---
source_url: https://docs.coze.cn/tutorial/channel_integration_tutorial
title: '入驻公共渠道 - 文档 - 扣子'
site: coze_cn
scraped_at: 2026-05-04T14:53:27Z
---

# 入驻公共渠道 - 文档 - 扣子

入驻公共渠道

本文介绍入驻扣子公共渠道的操作步骤。企业的超级管理员或管理员可以将企业的自定义渠道升级为公共渠道，以便智能体开发者将低代码智能体发布至公共渠道。​

说明

  * 套餐限制：扣子企业旗舰版、原企业版支持入驻公共渠道，单击[此处提交申请。](<https://bytedance.sg.larkoffice.com/share/base/form/shrlgcE3ieqZw9kjpWoF5bcllih>)​

  * 公共渠道数量限制：单个企业最多支持 1 个公共渠道。​

​

功能简介​

扣子编程提供标准的生态对接方式，支持网站、App、应用市场、硬件设备等厂商作为公共渠道入驻。低代码智能体开发者在扣子编程中搭建并发布低代码智能体到公共渠道之后，用户即可在对应渠道中与智能体对话。​

自定义渠道支持三种授权模式，渠道管理员可以根据业务场景和安全要求选择合适的方案。具体说明如下表所示。​

​

方案​| 无需授权​| 设备绑定授权​| OAuth 账号互通授权​  
---|---|---|---  
对接复杂度​| 低​| 中​| 高​  
应用场景​| 渠道仅作为内容分发平台，渠道侧不关心智能体的创建者是谁。​| 

  * 适用于拥有实体设备的渠道，如智能玩具、智能穿戴设备等。​

  * 渠道需将设备信息同步至扣子编程。​

  * 智能体开发者在发布时将其智能体与特定设备绑定。​

| 

  * 实现渠道用户与扣子用户的账号打通。​

  * 智能体开发者必须是渠道内的用户。​

  * 渠道和扣子的智能体开发者权限进行联动管理。​

  
渠道示例​| 穿山甲、小米应用​| FoloToy、机智云物联网、显眼包​| 豆包、飞书​  
  
​

渠道入驻的实现流程如下图所示。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27315.60693641618496%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjMxNS42MDY5MzY0MTYxODQ5NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

渠道管理员配置渠道入驻​

步骤一：创建渠道 OAuth JWT 应用​

组织超级管理员或管理员在扣子编程的 [Playground](<https://code.coze.cn/playground>) 页面选择授权 > OAuth 应用，创建一个渠道类型的 OAuth 应用，以便渠道侧调用扣子的 Open API 与智能体进行聊天等操作，具体请参见​OAuth JWT 授权（渠道场景）。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27298.8179669030733%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjI5OC44MTc5NjY5MDMwNzMzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27407.565011820331%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjQwNy41NjUwMTE4MjAzMzEiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48L3N2Zz4=)​

​

​

步骤二：创建自定义渠道​

在扣子编程的账号设置 > 发布渠道 > 企业自定义渠道管理页签中单击添加平台，设置自定义渠道的头像、渠道名称和描述，并绑定步骤一中创建的渠道 OAuth 应用，详细说明请参见​步骤二：渠道管理员添加发布渠道。​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27252.02312138728323%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI1Mi4wMjMxMjEzODcyODMyMyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

步骤三：配置 OAuth 授权​

在设备绑定授权和 OAuth 账号互通授权场景中，渠道侧需要获取设备信息或智能体开发者信息，需要根据对应的场景分别执行如下操作。​

场景一：无需授权​

在本场景中，无需进行额外的 OAuth 配置。​

场景二：设备绑定授权​

在设备绑定授权场景中，渠道侧需要获取设备信息，需要执行如下操作：​

1.

联系扣子商务经理开通渠道设备绑定能力。​

  * 创建自定义渠道后，你需要将自定义渠道的渠道 ID 提供给扣子商务经理，申请开通渠道设备绑定的能力，并由商务经理配置设备绑定的 key。​

2.

获取终端用户的 Access Token。​

  * 渠道侧通过​OAuth 授权码授权、​OAuth PKCE或​OAuth 设备授权获取终端用户的 Access Token。​

  * 以 OAuth PKCE 授权为例，操作方法如下，实现 PKCE 授权的详细示例代码请参见 [device_bind_connector/](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/custom_connector/device_bind_connector/app.py>)[app.py](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/custom_connector/device_bind_connector/app.py>)。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27202.98507462686567%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIwMi45ODUwNzQ2MjY4NjU2NyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27521.3930348258707%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjUyMS4zOTMwMzQ4MjU4NzA3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27232.8358208955224%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIzMi44MzU4MjA4OTU1MjI0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​

​

3.

绑定设备。​

  * 调用​绑定设备 Open API，将设备与自定义渠道绑定，示例代码请参见 [device_bind_connector/](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/custom_connector/device_bind_connector/app.py>)[app.py](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/custom_connector/device_bind_connector/app.py>)。​

  * 后续开发者发布智能体到自定义渠道时，在发布配置页面的设备列表中选择对应的设备，即可快速发布到对应设备。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27233.7962962962963%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIzMy43OTYyOTYyOTYyOTYzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

场景三：OAuth 账号互通授权配置​

在账号互通场景中，渠道侧需要获取智能体开发者信息，需要执行如下操作：​

1.

渠道侧实现 OAuth Server 授权服务。​

  * 渠道侧应具备 OAuth Server 的能力，向扣子服务端提供授权服务，需实现下表中的 3 个接口，详细说明请参见​步骤三：渠道管理员配置渠道授权。实现 OAuth 授权的示例代码请参见 [OAuth 账号互通授权示例代码](<https://github.com/coze-dev/coze-cookbook/blob/main/examples/custom_connector/oauth_connector/app.py>)。​

  * ​

接口​| 示例路径​| 使用场景​  
---|---|---  
授权页​| <host>/oauth/authorize​| 用户在扣子发布页面单击授权后，扣子自动重定向到该授权页。​  
获取 Token API​| <host>/oauth/token​| 授权完成后，扣子使用渠道 OAuth Server 生成的 Code，调用此接口获取 Access Token。​  
获取智能体开发者的用户信息 API​| <host>/oauth/user​| 获取 Access Token 后，调用此接口获取用户的 ID 和 Name，用于账号打通。​  
  
​

2.

在扣子编程配置渠道鉴权。​

  * 在扣子编程的账号设置 > 发布渠道 > 企业自定义渠道管理页签中，找到步骤二中添加的自定义渠道，配置 OAuth。​

  * 配置完成后，触发授权时，扣子编程会向渠道侧申请授权。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27270.2546296296297%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjI3MC4yNTQ2Mjk2Mjk2Mjk3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27242%27%20height=%27283%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQyIiBoZWlnaHQ9IjI4MyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

步骤四：订阅渠道回调​

企业超级管理员或管理员订阅渠道回调，获取对应自定义渠道中的回调信息，例如智能体发布至对应渠道、智能体从对应渠道下架、该渠道中产生的账单等。​

1.

在[回调管理](<https://www.coze.cn/open/callback/normal>)的渠道回调管理页面会展示已添加的自定义渠道，单击对应渠道卡片中的配置，配置回调地址。参数说明请参见前文​步骤一：创建回调应用。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27600%27%20height=%27357.22543352601156%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM1Ny4yMjU0MzM1MjYwMTE1NiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

2.

配置完成后单击确认，扣子服务器会向该回调地址发送一个用于校验地址有效性的 application/json 格式的 POST 请求。​

  * 回调的结构体示例如下：​

  * ​

JSON

复制

{​

"header": {​

"event_type": "url_verification",​

"event_id": "bee31258-469c-48a6-ae48-648161d89c79",​

"created_at": 1749116452112​

},​

"event": {​

"challenge": "988df7dc-2179-4dba-95a6-af9f40b91486"​

}​

}​

​

  * 开发者服务器接收该请求后，需要在 3s 内将challenge值（JSON格式）原样返回给扣子编程，否则请求地址验证将失败。​

  * 响应回调的结构体示例如下：​

  * ​

JSON

复制

{"challenge":"988df7dc-2179-4dba-95a6-af9f40b91486"}​

​

3.

单击对应渠道卡片中的订阅事件，在弹出的对话框中开启需要订阅的事件，可订阅的回调事件列表及其说明请参见​回调事件。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27500%27%20height=%27226.5717674970344%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjIyNi41NzE3Njc0OTcwMzQ0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

步骤五：上线公共渠道​

联系扣子商务经理，签署渠道入驻协议，并上线公共渠道。渠道管理员需要提供渠道 ID、渠道简要介绍，以便在公共渠道页面展示对应信息。​

获取渠道 ID​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27114.69194312796209%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjExNC42OTE5NDMxMjc5NjIwOSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

渠道简要介绍展示示例​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27106.1611374407583%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjEwNi4xNjExMzc0NDA3NTgzIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

​

跑通渠道入驻示例代码​

为方便渠道管理员快速完成渠道入驻，扣子提供了详细的示例代码，可以参考示例代码完成渠道入驻。​

1.

下载[渠道入驻示例代码](<https://github.com/coze-dev/coze-cookbook/tree/main/examples/custom_connector>)。​

2.

根据选择的授权模式，修改 .env 配置文件。​

  * 无需授权​

​

Bash

复制

CONNECTOR_CLIENT_ID=client_id_for_coze # 渠道分配给扣子的 client_id​

CONNECTOR_CLIENT_SECRET=client_secret_for_coze # 渠道分配给扣子的 client_secret​

CONNECTOR_USER_ID=connector_uid # 渠道的用户 uid​

CONNECTOR_USER_NAME=connector_name # 渠道的用户 name​

COZE_CALLBACK_TOKEN=3JZ9JrHhXMihsrFuCLqbPaxfqnN2JUVCIjpuarFsNxsI2aK1k9uVq6vYi4uBwKp6 # 扣子回调 token​

​

​

设备授权​

​

Bash

复制

CONNECTOR_ID=7470849514748805170 # 渠道 id​

CONNECTOR_PKCE_CLIENT_ID=30367348905137699749500653976611.app.coze # pkce client id​

CONNECTOR_CLIENT_ID=client_id_for_coze # 渠道分配给扣子的 client_id​

CONNECTOR_CLIENT_SECRET=client_secret_for_coze # 渠道分配给扣子的 client_secret​

CONNECTOR_USER_ID=connector_uid # 渠道的用户 uid​

CONNECTOR_USER_NAME=connector_name # 渠道的用户 name​

COZE_CALLBACK_TOKEN=3JZ9JrHhXMihsrFuCLqbPaxfqnN2JUVCIjpuarFsNxsI2aK1k9uVq6vYi4uBwKp6 # 扣子回调 token​

​

OAuth 账号互通授权​

​

Bash

复制

cd examples/custom_connector/device_bind_connector​

​

python -m venv ./.venv # 创建虚拟环境​

source .venv/bin/activate # 激活虚拟环境​

pip install -r requirements.txt # 安装依赖​

​

python app.py # 启动程序​

​

​

​

3.

安装所需的依赖包。​

a.

前往[扣子授权页面](<https://www.coze.cn/open/oauth/apps>)，单击渠道应用后面的下载按钮，将 coze_ oauth_config.json 下载到当前目录。​

b.

运行 app.py 文件。​

  * ​

Bash

复制

cd examples/custom_connector/device_bind_connector #进入对应目录，请根据实际修改​

​

python -m venv ./.venv # 创建虚拟环境​

source .venv/bin/activate # 激活虚拟环境​

pip install -r requirements.txt # 安装依赖​

​

python app.py # 启动程序​

​

  * 程序会启动一个 127.0.0.1:5000 的 HTTP 服务器，将该服务部署到公网环境，以便接收来自扣子编程的回调。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27700%27%20height=%27216.0693641618497%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzAwIiBoZWlnaHQ9IjIxNi4wNjkzNjQxNjE4NDk3IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

相关操作​

渠道侧审核智能体发布​

开发者将智能体发布到对应的渠道后，扣子服务端会向渠道侧发送​智能体发布回调事件。渠道侧收到回调事件后，应校验签名、从回调消息中提取信息，在渠道侧进行业务处理后，在响应中返回智能体的审核结果给扣子服务端，否则智能体发布失败。​

说明

如果审核流程无法在 10 秒内完成，自定义渠道可以先发送一条审核中的响应消息，审核结束后，再通过 API ​更新审核结果通知扣子此智能体的最终审核结果。​

​

​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27454%27%20height=%27416%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDU0IiBoZWlnaHQ9IjQxNiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==)​

​

​

Python

复制

# 在扣子发布智能体到渠道的时候，扣子会给本接口推送一条 json 数据，包含 bot 相关信息​

@app.route("/coze/callback", methods=["POST"])​

@log_request_response​

def coze_callback():​

# 获取签名和时间戳​

signature = request.headers.get("X-Coze-Signature")​

timestamp = request.headers.get("X-Coze-Timestamp")​

nonce = request.headers.get("X-Coze-Nonce")​

​

if not signature or not timestamp or not nonce:​

return jsonify({"code": 400, "message": "缺少签名或时间戳"}), 400​

​

# 获取请求体​

body = request.get_data().decode("utf-8")​

if not body:​

return jsonify({"code": 400, "message": "请求体为空"}), 400​

​

expected_signature = gen_coze_callback_signature(​

nonce, timestamp, body, COZE_CALLBACK_TOKEN​

)​

if signature != expected_signature:​

return jsonify({"code": 401, "message": "签名验证失败"}), 401​

​

event = json.loads(body)​

event_type = event.get("header", {}).get("event_type", "")​

# user_id = event.get("event", {}).get("user_id", "")​

# connector_user_id = event.get("event", {}).get("connector_user_id", "")​

bot_id = str(event.get("event", {}).get("bot_id", ""))​

bot_name = event.get("event", {}).get("bot_name", "")​

​

if event_type != "bot.published":​

return jsonify({"code": 400, "message": f"不支持处理事件 {event_type}"}), 400​

​

# audit_status: 1: 审核中；2: 通过；3: 拒绝​

if "非法" in bot_name or "违禁" in bot_name or "敏感" in bot_name:​

return jsonify({"audit": {"audit_status": 3, "reason": "bot 名称非法"}}), 200​

if "审核中" in bot_name:​

return jsonify({"audit": {"audit_status": 1, "reason": ""}}), 200​

​

save_bot(bot_id, bot_name)​

return jsonify({"audit": {"audit_status": 2, "reason": ""}}), 200​

​

管理智能体下架​

智能体下架包括开发者主动下架和渠道侧下架智能体两种场景，具体如下：​

  * 开发者下架智能体​

  * 企业超级管理员或管理员订阅渠道回调中的智能体下架事件后，开发者下架智能体时，渠道侧会收到​智能体下架回调事件，按需执行渠道侧的下架清理逻辑，例如删除智能体展示入口。​

  * 渠道侧下架智能体​

  * 渠道侧在审核智能体过程中如果发现智能体不符合规范，可以调用​下架智能体 API，输入下架原因，扣子会将该原因展示给开发者。​

  * ​

​​![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27400%27%20height=%27385.3211009174312%27/%3e)![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM4NS4zMjExMDA5MTc0MzEyIiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PC9zdmc+)​

​

查看智能体配置​

渠道管理员可以通过如下步骤查看智能体配置：​

1.

开发者发布智能体后，渠道侧从智能体发布回调事件中获取智能体的 ID 等信息。​

2.

调用​查看智能体配置 API，传入获取的智能体 ID，获取智能体的详细配置信息。​

​

上一篇

AI 教学场景的成员与资源管理

下一篇

为企业内 AI 应用选择发布渠道