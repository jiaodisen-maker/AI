import { DiscoveryForm } from "./DiscoveryForm";

export default function DiscoveryPage() {
  return (
    <div className="space-y-4 max-w-2xl">
      <h1 className="text-xl font-semibold">A1 Discovery</h1>
      <p className="text-sm text-zinc-500">
        触发批量发现 + 起 N 个 AgenticInsight workflow。<br />
        <strong>poc</strong> 通道走 MediaCrawler / DrissionPage（需 POC_CRAWLED_ENABLED=true）；
        <strong>prod</strong> 通道走抖音 OpenAPI + 巨量创意中心（需 OAuth 凭据）。
      </p>
      <DiscoveryForm />
    </div>
  );
}
