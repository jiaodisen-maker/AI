"""A5 Conversion Agent — W2 实装。

1) 自家账号：千川 Marketing API + 巨量算数 OAuth 拉视频维度数据（CPM / CTR / 完播率 / GMV）
2) 竞品 case（poc_crawled）：写 verdict='no_data'，confidence=0
3) 写 cross_validations.agent='a5_conversion'
"""
from temporalio import activity


@activity.defn
async def fetch_conversion(case_id: str) -> None:
    raise NotImplementedError("A5 Conversion — W2 deliverable")
