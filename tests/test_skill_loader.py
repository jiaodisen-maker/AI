"""SKILL.md 文件系统加载器测试"""
import pytest

from app.adapters.impls.skill_loader import FilesystemSkillLoader


@pytest.fixture
def skills_dir(tmp_path):
    """创建临时 skills 目录"""
    # Skill 1
    s1 = tmp_path / "compliant-copy"
    s1.mkdir()
    (s1 / "SKILL.md").write_text(
        "---\n"
        "name: compliant-copy\n"
        "description: 为保健品生成合规文案\n"
        "triggers: [写文案, 合规文案]\n"
        "---\n"
        "# 合规文案 Skill\n\n"
        "禁词清单：治疗 / 治愈 / 根治\n",
        encoding="utf-8",
    )

    # Skill 2
    s2 = tmp_path / "data-query"
    s2.mkdir()
    (s2 / "SKILL.md").write_text(
        "---\n"
        "name: data-query\n"
        "description: 查询销售数据\n"
        "triggers: [查数据, 销售]\n"
        "---\n"
        "# 数据查询\n",
        encoding="utf-8",
    )

    # 无效 skill（无 frontmatter）
    s3 = tmp_path / "invalid"
    s3.mkdir()
    (s3 / "SKILL.md").write_text("# 没有 frontmatter\n", encoding="utf-8")

    return tmp_path


@pytest.mark.asyncio
async def test_load_skills_count(skills_dir):
    loader = FilesystemSkillLoader()
    n = await loader.load_skills(str(skills_dir))
    assert n == 2  # 只有 2 个有效


@pytest.mark.asyncio
async def test_get_skill(skills_dir):
    loader = FilesystemSkillLoader()
    await loader.load_skills(str(skills_dir))

    skill = await loader.get_skill("compliant-copy")
    assert skill is not None
    assert skill.description == "为保健品生成合规文案"
    assert "写文案" in skill.triggers
    assert "禁词清单" in skill.instructions


@pytest.mark.asyncio
async def test_match_skill_by_trigger(skills_dir):
    loader = FilesystemSkillLoader()
    await loader.load_skills(str(skills_dir))

    matched = await loader.match_skill("帮我写文案")
    assert matched is not None
    assert matched.name == "compliant-copy"

    matched2 = await loader.match_skill("查一下销售情况")
    assert matched2 is not None
    assert matched2.name == "data-query"


@pytest.mark.asyncio
async def test_skills_prompt(skills_dir):
    loader = FilesystemSkillLoader()
    await loader.load_skills(str(skills_dir))

    prompt = await loader.get_skills_prompt()
    assert "compliant-copy" in prompt
    assert "data-query" in prompt


@pytest.mark.asyncio
async def test_auto_reload_on_mtime_change(skills_dir, monkeypatch):
    """文件修改后自动重新加载"""
    loader = FilesystemSkillLoader()
    await loader.load_skills(str(skills_dir))

    skill = await loader.get_skill("compliant-copy")
    assert "禁词清单" in skill.instructions

    # 修改文件
    skill_file = skills_dir / "compliant-copy" / "SKILL.md"
    new_content = (
        "---\n"
        "name: compliant-copy\n"
        "description: 升级版描述\n"
        "triggers: [写文案]\n"
        "---\n"
        "# v2 内容\n"
    )
    skill_file.write_text(new_content, encoding="utf-8")

    # 模拟 mtime 推进
    import os
    new_mtime = skill_file.stat().st_mtime + 100
    os.utime(skill_file, (new_mtime, new_mtime))

    # 重新获取应该返回新版本
    updated = await loader.get_skill("compliant-copy")
    assert updated.description == "升级版描述"
