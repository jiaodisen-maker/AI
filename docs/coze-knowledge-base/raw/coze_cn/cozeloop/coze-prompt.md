---
source_url: https://docs.coze.cn/cozeloop/coze-prompt
title: '管理扣子提示词 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:54:10Z
---

# 管理扣子提示词 - 文档 - 扣子

管理扣子提示词

扣子罗盘与扣子工作流（Workflow）的提示词支持互通，用户可以在罗盘对提示词进行调优、版本管理，并在工作流中关联应用调优后的提示词，同时支持用户在工作流开发过程中，新增扣子罗盘的提示词，提升提示词管理效率。​

应用场景​

  * 提示词复用与管理：开发工作流时，用户可以直接关联罗盘中已经调优好的提示词，避免重复创建和优化，确保提示词质量和一致性，当关联的罗盘提示词版本更新时，用户可以自由切换版本，提高开发效率。​

  * 提示词版本控制：用户需要对工作流中的提示词进行迭代优化时，可以利用罗盘的提示词版本管理能力，在不同版本间切换，或提交新版本，保持提示词的可追溯性和可管理性。​

  * 跨平台协同优化：用户可以在罗盘中精细调优提示词，在工作流中直接应用；也可以在工作流中修改提示词后，将其作为新版本提交到罗盘，实现两个平台间的协同优化。​

在扣子工作流中关联罗盘提示词​

在扣子工作流的大模型节点中，开发者可以填写系统提示词和用户提示词，这些提示词会在调用节点时被传递被大模型。大模型节点的系统提示词支持引用扣子罗盘中已创建、调优并提交版本的提示词，开发者无需在大模型节点中通过试运行节点来调试和编辑提示词。​

说明

  * 工作流中只有大模型节点的系统提示词支持关联扣子罗盘提示词。​

  * 工作流与扣子罗盘提示词必须处于同一工作空间内，才可以关联。​

  * 罗盘提示词中已有的变量，会自动添加到工作流编排 > 输入 > 变量区域。​

  * 扣子罗盘不支持技能（工具、工作流、知识库）调试，因此如果在开发工作流时关联罗盘提示词，并在提示词内插入技能，在扣子罗盘侧依然能够展示技能信息，但不支持对技能进行编辑、调试，仅支持删除技能。​

​

在扣子工作流中引用罗盘提示词的操作步骤如下：​

1.

在扣子开发平台中打开或创建一个工作流。​

2.

添加或选择一个大模型节点。​

3.

在系统提示词编辑区域，点击上方工具栏的罗盘图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27428%27%20height=%27234%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDI4IiBoZWlnaHQ9IjIzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

根据页面提示，在提示词库中找到提示词。​

  * 提示词库中支持搜索你在扣子罗盘同一工作空间中已创建、调优并提交版本的提示词。选择提示词后，右上角还可以切换提示词的不同版本。如果没有合适的提示词，你也可以在页面右上角单击新建提示词。​

  * 说明

仅支持关联罗盘提示词中的首个系统提示词（System Prompt），如果罗盘提示词中没有系统提示词，则详情页面为空。​

​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27452%27%20height=%27247%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDUyIiBoZWlnaHQ9IjI0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

5.

在提示词库页面中，将扣子罗盘提示词添加到系统提示词。​

  * 支持以下两种添加方式：​

  * 关联并覆盖：将罗盘提示词的内容填充到工作流提示词编辑区域，并覆盖工作流原本系统提示词内容​

  * 关联并插入：在工作流原本系统提示词内容之后，插入罗盘提示词​

6.

关联成功后，编辑区域上方会显示关联状态，包含提示词名称和版本信息。​

  * 你也可以根据页面提示切换版本，切换版本后会对当前提示词进行覆盖。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27537%27%20height=%27294%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM3IiBoZWlnaHQ9IjI5NCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在工作流中提交罗盘提示词新版本​

在大模型节点中成功引用罗盘提示词后，如果你系统提示词编辑区域中进行二次编辑，系统会自动创建一个草稿版本，但这个草稿版本不会自动同步到扣子罗盘，你需要手动单击提交按钮，在工作流提交罗盘提示词的新版本。​

1.

在工作流大模型节点系统提示词编辑区域编辑罗盘提示词。​

2.

单击提交按钮。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27488%27%20height=%27267%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg4IiBoZWlnaHQ9IjI2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

查看不同版本的提示词文本差异，并提交新版本。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27484%27%20height=%27265%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDg0IiBoZWlnaHQ9IjI2NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27394%27%20height=%27216%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk0IiBoZWlnaHQ9IjIxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

4.

点击关联罗盘提示词名称右侧的跳转链接，可见提示词版本已经更新。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27538%27%20height=%27295%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTM4IiBoZWlnaHQ9IjI5NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27399%27%20height=%27218%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzk5IiBoZWlnaHQ9IjIxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

在工作流中新增罗盘提示词​

在工作流大模型节点的系统提示词中关联罗盘提示词时，如果没有合适的提示词，你可以参考以下流程，在工作流中创建一个新的罗盘提示词。​

1.

在工作流系统提示词编辑区域，点击上方工具栏的罗盘图标。​

2.

在弹出的扣子罗盘提示词库弹窗中，根据页面提示单击新建提示词。​

  * 新建完成的提示词将在扣子罗盘侧也同步更新。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27517%27%20height=%27283%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTE3IiBoZWlnaHQ9IjI4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

3.

在新建提示词表单中填写以下信息：​

  * 提示词Key（必填）​

  * 提示词名称（必填）​

  * 提示词描述（选填）​

  * 提示词内容（选填）​

  * 支持拉取当前工作流系统提示词的内容，填充到提示词内容区域​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27506%27%20height=%27276%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA2IiBoZWlnaHQ9IjI3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

点击确认，完成创建。​

  * 创建完成后即可在扣子罗盘提示词库看到新建的提示词，然后你就可以在工作流中关联这个新的提示词。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27505%27%20height=%27276%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTA1IiBoZWlnaHQ9IjI3NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

在工作流中解除罗盘提示词关联关系​

如果大模型节点的系统提示词不再需要使用扣子罗盘提示词，你可以在大模型节点中解除关联关系。​

操作步骤如下：​

1.

在系统提示词的编辑界面，点击上方工具栏的解除关联图标。​

2.

在弹出的二次确认弹窗中，点击解除，取消工作流与罗盘提示词的关联。​

  * 取消关联后，罗盘提示词的内容会保留，但不再与罗盘提示词关联。​

  * 系统提示词编辑区域上方的关联信息将消失。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27657%27%20height=%27359%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU3IiBoZWlnaHQ9IjM1OSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

常见问题​

Q1：关联罗盘提示词后，我还能在工作流中直接编辑提示词内容吗？​

A1：可以。关联后用户仍然可以在工作流系统提示词编辑区域，修改提示词内容。但修改后，建议用户提交为罗盘提示词的新版本，便于持续维护与迭代。​

Q2：如果关联的罗盘提示词被删除了，会怎样？​

A2：如果关联的罗盘提示词被删除，工作流中已经填充的提示词内容不会受影响，但系统会自动解除关联关系。下次打开工作流系统提示词编辑界面时，会有异常提示，可以选择关联其他罗盘提示词。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27586%27%20height=%27320%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg2IiBoZWlnaHQ9IjMyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

Q3：一个罗盘提示词可以关联多个工作流吗？​

A3：可以。一个罗盘提示词可以被多个工作流关联。​

Q4：一个工作流可以关联多个罗盘提示词吗？​

A4：不可以。一个工作流只能关联一个罗盘提示词。​

Q5：复制已经关联罗盘提示词的工作流，可以保留与罗盘提示词的关联关系吗？​

A5：如果工作流在同空间内复制，关联关系会同步复制，在新的副本工作流中，依然可以看到与罗盘提示词的关联关系；如果工作流跨空间复制，则无法保留关联关系，但是工作流中已经填充的提示词内容不会受影响。​

Q6：工作流中修改提示词并提交新版本后，其他关联该提示词的工作流会自动更新吗？​

A6：不会自动更新。其他工作流仍然使用它们之前关联的版本。如果希望使用最新版本，需要在各个工作流中手动切换到最新版本。​

Q7：被关联的罗盘提示词提交新版本后，其他关联该提示词的工作流会自动更新吗？​

A7：不会自动更新。其他工作流仍然使用它们之前关联的版本。如果希望使用最新版本，需要在各个工作流中手动切换到最新版本。​

Q8：工作流关联罗盘提示词后，在提示词新增使用罗盘不支持的变量类型（如zip、excel等）和技能，并提交新版本时，会有什么影响？​

A8：系统会完整保留提示词中的变量和技能调用。在工作流执行时，这些变量和技能调用会正常解析和执行。在罗盘中查看或编辑时，也会保留这些特殊元素的原始格式，但是不支持编辑、调试，仅支持删除。​

Q9：关联罗盘提示词时，打开的提示词库为空​

A8：首先检查工作流与想要关联的罗盘提示词，是否在同一个工作空间，或者扣子罗盘当前空间内是否有提示词。​

​

​

上一篇

管理提示词版本

下一篇

配置模型