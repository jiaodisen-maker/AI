---
source_url: https://docs.coze.cn/guides/image_generation_node_announcement
title: '关于图像生成节点调整的公告 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:28:22Z
---

# 关于图像生成节点调整的公告 - 文档 - 扣子

关于图像生成节点调整的公告

随着生图场景热度的不断攀升，工作流图像生成节点的通用/通用-Pro 模型已无法在用量高峰时段满足海量用户稳定运行的需求，通用/通用-Pro 模型将于 2025 年 10 月 25 日全量下线。​

近期扣子团队收到了许多关于此次变更的意见与反馈，我们非常重视大家的每一条声音，并已第一时间在团队内进行了深入复盘。现正式对图像生成节点的调整计划做出如下更新。​

10月15日前维持原并发限制​

为尽可能减少对现有工作流的影响，旧的生图插件（工作流-图像生成节点）的并发限制已临时恢复为单账号 4 并发。在 10 月 15 日之前，扣子用户可继续正常使用图像生成节点，预留出更长时间以供用户便捷升级。​

图像生成节点模型升级方案​

扣子团队已完成图像生成节点升级，该节点现正式支持 Seedream 4.0 模型，为保障你的线上业务不受影响，请尽快将当前使用通用/通用-Pro 模型的存量图像生成节点切换到 Seedream 4.0 模型。Seedream 4.0 模型能够灵活应对复杂的多模态生成任务，新增知识生图、复杂推理和参考图一致性等功能，推理速度较前代大幅提升，并支持高达 4K 高清精美图像生成。更多信息，请参考 ​Seedream 模型生图教程。​

此次升级操作简便，你仅需在节点内切换模型即可完成升级，无需调整参数内容，且输入/输出参数将基本保持一致，避免对已有提示词的大规模调整。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27679%27%20height=%27350%27/%3e)![](https://p9-arcosite.byteimg.com/https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a04e4fbc4cc44e898f6bdc74619734cd~tplv-goo7wpa0wc-quality:q75.image)​

​

为了进一步提升切换工作的平稳性，建议先复制图像生成节点，对比通用/通用-Pro 模型和 Seedream 4.0 模型的生图效果后，再进行切换。具体操作流程如下：​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27681%27%20height=%2768%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjgxIiBoZWlnaHQ9IjY4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

1.

复制图像生成节点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27273%27%20height=%27147%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjczIiBoZWlnaHQ9IjE0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

切换新图像生成节点到 Seedream 4.0 模型。​

  * 在新图像生成节点中，选择 Seedream 4.0 模型，检查其他参数与旧图像生成节点一致，例如结果图的比例、尺寸等配置。​

  * 工作流​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27251%27%20height=%2781%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUxIiBoZWlnaHQ9IjgxIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

新图像生成节点​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27271%27%20height=%27338%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcxIiBoZWlnaHQ9IjMzOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

结束节点​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27270%27%20height=%27209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjcwIiBoZWlnaHQ9IjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

3.

验证新图像生成节点生成效果。​

  * 基于相同的参考图和提示词，新图像生成节点生成了 1024*1024 大小的人物图像，符合工作流原来的生图需求。同时，在生成效果上显著优于旧图像生成节点。​

  * 参考图和提示词​

  * ​

Plain Text

复制

参考画面中的人物姿势，生成一个真实的元气女孩图片​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27245%27%20height=%27404%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ1IiBoZWlnaHQ9IjQwNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

旧图像生成节点（通用模型）​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27264%27%20height=%27264%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjY0IiBoZWlnaHQ9IjI2NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

新图像生成节点（Seedream 4.0 模型）​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27246%27%20height=%27246%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ2IiBoZWlnaHQ9IjI0NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

4.

删除旧图像生成节点。​

  * 删除旧节点后，需将引用到旧图像生成节点的后续节点变量，改为引用新图像生成节点。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27707%27%20height=%27121%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzA3IiBoZWlnaHQ9IjEyMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

发布工作流。​

  * 至此，完成从通用/通用-Pro 模型到 Seedream 4.0 模型的切换。​

模型效果对比​

通用/通用-Pro 模型和 Seedream 4.0 模型在文生图、图生图等场景的效果对比如下：​

​

分类​| 原始图片及提示词​| 通用/通用-Pro 模型效果图​| Seedream 4.0 模型效果图​  
---|---|---|---  
文生图​| ​Plain Text复制采用雷蒙德·布里格斯（Raymond Briggs）和马蒂亚斯·阿道夫松（Mattias Adolfsson）风格的插画，白色简洁背景，运用钢笔与水彩混合媒介创作，小兔子上幼儿园的一系列插画​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%271024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272048%27%20height=%272048%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA0OCIgaGVpZ2h0PSIyMDQ4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
图生图（人像-人物一致）​| ​Plain Text复制将主体从站着改成坐着​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%271024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%272048%27%20height=%272048%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjA0OCIgaGVpZ2h0PSIyMDQ4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​  
图生图（空间深度）​​| ​Plain Text复制参考画面的空间关系生成一名男性站在草地上​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%271024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%271024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
图生图（人物姿势）​| ​Plain Text复制参考画面的人物姿势生成一只猴子站在树上​​​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27200%27%20height=%27200%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%271024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​| ​​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%271024%27%20height=%271024%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAyNCIgaGVpZ2h0PSIxMDI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​​​  
  
​

专项支持通道​

如遇个别兼容性或效果问题，可联系[火山智能客服](<https://console.volcengine.com/common-buy/veCoze_Pro||cv758gvog65oe0kcjir0?openVcopilot={"query":"","displayMode":"fullscreen"}&entry=OfficialSideBar>)反馈，我们将协助排查解决。​

常见问题​

关于本次插件调整的几个高频问题的解答如下：​

Q1：为什么要做调整？​

A：原插件在稳定性和高并发支持上存在一定限制，随着该插件使用量的不断提升，在高峰时段已难以满足高效稳定运行的需求。为提供更可靠、更适合商用的服务，新插件已接入了火山方舟一致的资源与服务治理体系。确保服务具备更好的稳定性与扩展性，价格方面也与火山方舟官方保持统一。​

Q2：新插件有哪些优势？​

A：新插件和原有插件底层的基座模型是一致的，新插件在并发支持、故障容错和服务可用性方面也有显著增强，尤其适合生产环境长期、稳定调用，能为高负载应用提供更可靠的保障。​

Q3：还提供免费额度吗？​

A：免费额度依然保留，欢迎大家继续测试和验证效果。具体来说，[智能绘图_文生图](<https://www.coze.cn/store/plugin/7516843480623382568?from=add_plugin_menu>)、[文生图_seedream3](<https://www.coze.cn/store/plugin/7537296298148675622>)、​图像生成节点均为每个账号提供免费生成额度，详细规则可查阅官方文档​插件费用。​

Q4：用量较大能否申请优惠？​

A：可以申请。企业类用量较大的客户，欢迎联系自己的销售沟通折扣。若无销售对接，可以在[火山工单](<https://www.volcengine.com/docs/84458/>)联系咨询。​

​

​

上一篇

扣子订阅套餐升级公告

下一篇

对话流 API 请求参数校验调整的公告