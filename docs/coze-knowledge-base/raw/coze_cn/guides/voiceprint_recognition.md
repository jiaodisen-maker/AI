---
source_url: https://docs.coze.cn/guides/voiceprint_recognition
title: '声纹识别 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:33:00Z
---

# 声纹识别 - 文档 - 扣子

声纹识别

声纹识别可以提取说话人的声音特征和说话内容信息，实现自动核验说话人身份的功能。在进行声纹识别时，扣子编程会在声纹组内进行查找匹配对应的声纹，如果高于命中阈值，则认为是同一个人的声音。声纹识别适用于音视频通话场景，能够识别对话人的身份。​

功能简介​

开发者在智能体中开启声纹识别并配置声纹识别变量，借助声纹组和声纹数据来管理不同用户的声纹信息。在音视频通话时，扣子编程根据智能体绑定的声纹组，从声纹组中匹配说话人的身份，并将匹配到的身份信息传递给智能体。智能体依据身份信息，为用户提供个性化、安全且高效的交互体验。其主要应用场景包括：​

  * 智能家居控制：在智能手机、智能家居等终端设备中，声纹识别可用于精准的语音身份授权。系统仅响应已授权人员的声纹特征指令，有效屏蔽外界噪音干扰和非授权声音指令，确保设备操作的安全性和准确性。​

  * 家庭智能设备：通过声纹识别区分家庭成员，为不同用户身份提供专属服务和个性化内容，提升家庭智能设备的交互体验。​

  * 智能办公：在会议记录等办公场景中，声纹识别可实现发言人身份的动态区分。例如，智能会议系统通过声纹特征识别不同参会者身份，实时标注发言内容并生成结构化会议记录，提升会后资料整理效率。​

使用限制​

  * 默认最多可创建 1000 个声纹组。如需提高配额，请升级至扣子企业旗舰版，并联系对应销售申请扩容。​

  * 每个声纹组中最多可创建 10 个声纹。​

费用说明​

开启声纹识别功能后，用户与智能体进行音视频通话时，将产生声纹识别费用，详细费用说明可参考​音视频费用。​

步骤一：创建声纹​

1 创建声纹组​

声纹组是声纹的集合单元，例如，你可以为每个设备分别创建一个声纹组。​

说明

角色限制：组织超级管理员或管理员。​

​

1.

在[扣子编程](<https://code.coze.cn/home>)左下角单击个人头像，选择企业，然后单击对应组织的设置图标。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27313%27%20height=%27275%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzEzIiBoZWlnaHQ9IjI3NSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

2.

在企业组织管理页面的顶部选择声纹管理页签。​

3.

单击右上角的 ＋ 声纹组，填写声纹组的名称和描述，单击确认。​

2 创建声纹​

1.

单击对应的声纹组，进入声纹组详情页，单击右上角的 \+ 声纹。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27133.33333333333331%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjEzMy4zMzMzMzMzMzMzMzMzMSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在创建声纹页面，设置声纹的名称和描述，然后单击下一步。​

3.

单击上传声音或开始录制来记录声音特征。​

  * 上传声音：上传本地预先录制好的音频文件。音频文件需符合系统规定的格式和时长要求，以确保声纹提取的准确性，具体要求请参见页面中的说明。​

  * 开始录制：朗读系统提供的文案，根据现场录制的音频来记录声音特征。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27293.98148148148147%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI5My45ODE0ODE0ODE0ODE0NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

4.

单击试听图标，确认声音符合预期后，单击记录声纹。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27310.18518518518516%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjMxMC4xODUxODUxODUxODUxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤二：声纹测试​

通过声纹测试可以评估声纹识别的准确率。你可以上传测试音频，扣子编程将根据该测试音频与声纹库中已有的声纹进行对比，计算相似度，从而评估声纹识别系统在不同环境和条件下的匹配效果，确保精准度达到预期。此外，测试结果可用于调整命中阈值等参数，以更好地实现身份验证和个性化服务。​

1.

单击对应的声纹组，进入声纹组详情页，单击右上角的声纹测试。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27133.96674584323037%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjEzMy45NjY3NDU4NDMyMzAzNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

在声纹测试页面，设置命中阈值，单击上传声音或开始录制。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27271.412037037037%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI3MS40MTIwMzcwMzcwMzciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

  * 命中阈值是指声音匹配度的最低标准。当声音匹配度达到或超过该阈值时，扣子编程才会认定声纹匹配成功，确认为同一人的声音。取值范围：0~100，默认值：40。​

步骤三：在低代码智能体中开启声纹识别​

创建声纹后，可以将声纹组绑定至低代码智能体。在语音通话过程中，扣子编程能够从声纹组中匹配说话人的身份，并将匹配到的身份信息传递至智能体。智能体依据声纹信息，可实现差异化响应。例如：识别每次对话中对话人的身份、 根据不同身份进行个性化回复内容、特定人的声纹才可唤醒智能体进行对话等。​

1.

为低代码智能体开启声纹识别。​

a.

在智能体的编排页面，在对话体验 ＞ 音视频区域，单击 + 添加语音并设置音色。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27290.81500646830534%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI5MC44MTUwMDY0NjgzMDUzNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

b.

开启声纹识别，并设置命中阈值和空值时是否沿用历史。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27479.7453703703703%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjQ3OS43NDUzNzAzNzAzNzAzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

  * ​

参数​| 说明​  
---|---  
命中阈值​| 设置声音匹配度的最低标准。当声音匹配度达到或超过该阈值时，扣子编程才会认定声纹匹配成功。你可以根据应用的安全性要求进行自定义设置。如果匹配了多轮声纹，扣子编程会取相似度最高的一个。​取值范围：0~100，默认值：40。​  
声纹空值时沿用历史​| 当未命中任何一个声纹时，智能体将返回上一次命中的声纹。此选项适用于连续对话场景，当收音不好等情况导致声纹没能正确被识别时，开启该选项可确保对话的连贯性。​  
  
​

2.

在低代码智能体对话流中引用声纹变量。​

  * 开启声纹识别后，扣子编程会自动添加声纹识别的系统变量 sys_voiceprint_name 和 sys_voiceprint_info。变量的说明和配置示例如下：​

  * ​

变量​| 说明​  
---|---  
sys_voiceprint_name​| 声纹名称，用于标识对话人的身份，例如爸爸、妈妈等。​  
sys_voiceprint_info​| 声纹的其他携带信息，由用户自己定义，例如你可以添加用户偏好设置。​  
  
​

a.

在输入参数中添加 sys_voiceprint_name 参数，对应的值引用智能体中添加的系统变量 sys_voiceprint_name。​

b.

在用户提示词中，设置并引用变量 sys_voiceprint_name。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27658.880778588808%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjY1OC44ODA3Nzg1ODg4MDgiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

3.

在预览与调试页面，单击通话图标，选择对应的声纹组，以便在调试过程中验证声纹识别的效果。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27350%27%20height=%27349.4127516778523%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUwIiBoZWlnaHQ9IjM0OS40MTI3NTE2Nzc4NTIzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

4.

将智能体发布到 API 渠道。​

步骤四：使用声纹识别​

通过 [Real-Time SDK](<https://www.coze.cn/open/playground/rtcsdk>) 体验智能音视频通话时，指定对应的智能体和声纹组，扣子编程能够根据你的声纹特征进行识别，并据此提供差异化的响应，以实现个性化交互。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27613.9927623642943%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjYxMy45OTI3NjIzNjQyOTQzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

上一篇

快捷指令

下一篇

音视频通话