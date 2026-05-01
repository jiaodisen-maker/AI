"""initial 10 tables for v6 agentic insight system

Revision ID: 001
Revises:
Create Date: 2026-05-01

包含 §14.2 的全部 10 张表 + pgvector 扩展 + data_lineage trigger（§14.0 PoC/生产隔离硬约束）

"""
from typing import Sequence, Union

from alembic import op


revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    # ---------- 1. cases ----------
    op.execute(
        """
        CREATE TABLE cases (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            url TEXT NOT NULL,
            platform TEXT,
            brand TEXT,
            sku TEXT,
            category TEXT,
            duration_sec INT,
            likes INT,
            comments INT,
            gmv_estimated NUMERIC,
            raw_meta JSONB,
            discovered_by TEXT,
            data_lineage TEXT NOT NULL CHECK (data_lineage IN ('poc_crawled','oauth','public_api','manual')),
            poc_purge_at TIMESTAMPTZ,
            ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            workflow_id TEXT
        )
        """
    )
    op.execute("CREATE INDEX idx_cases_data_lineage ON cases (data_lineage)")
    op.execute("CREATE INDEX idx_cases_poc_purge_at ON cases (poc_purge_at) WHERE data_lineage = 'poc_crawled'")
    # constraint: poc_crawled rows must have purge date
    op.execute(
        """
        ALTER TABLE cases ADD CONSTRAINT poc_crawled_requires_purge_date
            CHECK (data_lineage <> 'poc_crawled' OR poc_purge_at IS NOT NULL)
        """
    )

    # ---------- 2. case_segments ----------
    op.execute(
        """
        CREATE TABLE case_segments (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            case_id UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
            segment_type TEXT NOT NULL,
            start_sec NUMERIC,
            end_sec NUMERIC,
            asr_text TEXT,
            ocr_text TEXT,
            visual_desc TEXT,
            llm_analysis JSONB
        )
        """
    )
    op.execute("CREATE INDEX idx_case_segments_case_id ON case_segments (case_id)")

    # ---------- 3. atoms ----------
    op.execute(
        """
        CREATE TABLE atoms (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            atom_type TEXT NOT NULL CHECK (atom_type IN ('hook','pain','trust','cta')),
            content TEXT NOT NULL,
            embedding vector(1024),
            microtype_ids UUID[],
            compliance_grade CHAR(1) CHECK (compliance_grade IN ('G','Y','R')),
            feasibility_4d JSONB,
            ctr_history NUMERIC,
            source_case_id UUID REFERENCES cases(id) ON DELETE SET NULL,
            source_segment_id UUID REFERENCES case_segments(id) ON DELETE SET NULL,
            created_by_agent TEXT
        )
        """
    )
    op.execute(
        "CREATE INDEX idx_atoms_embedding ON atoms USING ivfflat (embedding vector_cosine_ops)"
    )
    op.execute("CREATE INDEX idx_atoms_atom_type ON atoms (atom_type)")
    op.execute("CREATE INDEX idx_atoms_source_case_id ON atoms (source_case_id)")

    # ---------- 4. microtypes ----------
    op.execute(
        """
        CREATE TABLE microtypes (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            scene TEXT NOT NULL,
            audience TEXT NOT NULL,
            ingredient TEXT NOT NULL,
            emotion TEXT NOT NULL,
            restriction TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','candidate','deprecated')),
            proposed_by_agent BOOLEAN NOT NULL DEFAULT FALSE,
            UNIQUE (scene, audience, ingredient, emotion, restriction)
        )
        """
    )

    # ---------- 5. cross_validations ----------
    op.execute(
        """
        CREATE TABLE cross_validations (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            case_id UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
            agent TEXT NOT NULL CHECK (agent IN ('a3_compliance','a4_userpain','a5_conversion','a7_feasibility')),
            verdict TEXT,
            confidence NUMERIC,
            raw_data JSONB,
            validated_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
        """
    )
    op.execute("CREATE INDEX idx_cross_validations_case_id ON cross_validations (case_id)")

    # ---------- 6. generated_scripts ----------
    op.execute(
        """
        CREATE TABLE generated_scripts (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            microtype_id UUID NOT NULL REFERENCES microtypes(id),
            atom_ids UUID[] NOT NULL,
            prompt_version TEXT NOT NULL,
            output TEXT NOT NULL,
            llm_model TEXT NOT NULL,
            for_internal_research_only BOOLEAN NOT NULL DEFAULT FALSE,
            generated_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
        """
    )
    op.execute("CREATE INDEX idx_generated_scripts_microtype_id ON generated_scripts (microtype_id)")
    op.execute(
        "CREATE INDEX idx_generated_scripts_internal_only ON generated_scripts (for_internal_research_only)"
    )

    # ---------- 7. critic_scores ----------
    op.execute(
        """
        CREATE TABLE critic_scores (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            target_id UUID NOT NULL,
            target_type TEXT NOT NULL CHECK (target_type IN ('case','generated_script','atom')),
            evaluator_model TEXT NOT NULL,
            scores JSONB NOT NULL,
            reasoning TEXT,
            confidence NUMERIC,
            scored_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
        """
    )
    op.execute("CREATE INDEX idx_critic_scores_target ON critic_scores (target_type, target_id)")

    # ---------- 8. prompt_versions ----------
    op.execute(
        """
        CREATE TABLE prompt_versions (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            agent TEXT NOT NULL CHECK (agent IN ('a2','a8')),
            version TEXT NOT NULL,
            prompt_text TEXT NOT NULL,
            trigger_critic_id UUID REFERENCES critic_scores(id),
            metric JSONB,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            UNIQUE (agent, version)
        )
        """
    )

    # ---------- 9. hitl_alerts ----------
    op.execute(
        """
        CREATE TABLE hitl_alerts (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            alert_type TEXT NOT NULL CHECK (alert_type IN ('low_confidence','new_microtype','compliance_edge','poc_purge_failed')),
            payload JSONB NOT NULL,
            status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open','resolved')),
            resolved_by TEXT,
            resolved_at TIMESTAMPTZ,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
        """
    )
    op.execute("CREATE INDEX idx_hitl_alerts_status ON hitl_alerts (status)")

    # ---------- 10. userpain_clusters ----------
    op.execute(
        """
        CREATE TABLE userpain_clusters (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            cluster_label TEXT NOT NULL,
            representative_quotes TEXT[] NOT NULL,
            embedding vector(1024),
            source_count INT NOT NULL DEFAULT 0,
            imported_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
        """
    )
    op.execute(
        "CREATE INDEX idx_userpain_clusters_embedding ON userpain_clusters USING ivfflat (embedding vector_cosine_ops)"
    )

    # ============================================================
    # data_lineage trigger（PoC/生产 schema 级隔离的硬约束）
    # generated_scripts 引用了 atom，atom.source_case_id 必须满足：
    #   若 case.data_lineage = 'poc_crawled' → generated_scripts.for_internal_research_only 必须 = TRUE
    # 否则 RAISE EXCEPTION，阻止 PoC 数据进入对外发布通路。
    # ============================================================
    op.execute(
        """
        CREATE OR REPLACE FUNCTION enforce_poc_isolation()
        RETURNS TRIGGER AS $$
        DECLARE
            referenced_atom_id UUID;
            atom_source_case UUID;
            case_lineage TEXT;
        BEGIN
            IF NEW.atom_ids IS NULL OR array_length(NEW.atom_ids, 1) = 0 THEN
                RETURN NEW;
            END IF;

            FOREACH referenced_atom_id IN ARRAY NEW.atom_ids LOOP
                SELECT source_case_id INTO atom_source_case FROM atoms WHERE id = referenced_atom_id;
                IF atom_source_case IS NULL THEN CONTINUE; END IF;
                SELECT data_lineage INTO case_lineage FROM cases WHERE id = atom_source_case;

                IF case_lineage = 'poc_crawled' AND NEW.for_internal_research_only = FALSE THEN
                    RAISE EXCEPTION 'PoC isolation violation: generated_script % references atom from poc_crawled case % but for_internal_research_only is FALSE',
                        NEW.id, atom_source_case
                        USING ERRCODE = '23514';
                END IF;
            END LOOP;

            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """
    )
    op.execute(
        """
        CREATE TRIGGER trg_enforce_poc_isolation
            BEFORE INSERT OR UPDATE ON generated_scripts
            FOR EACH ROW EXECUTE FUNCTION enforce_poc_isolation()
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS trg_enforce_poc_isolation ON generated_scripts")
    op.execute("DROP FUNCTION IF EXISTS enforce_poc_isolation()")
    for tbl in [
        "userpain_clusters",
        "hitl_alerts",
        "prompt_versions",
        "critic_scores",
        "generated_scripts",
        "cross_validations",
        "microtypes",
        "atoms",
        "case_segments",
        "cases",
    ]:
        op.execute(f"DROP TABLE IF EXISTS {tbl} CASCADE")
