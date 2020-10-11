try:
    import requests
except ImportError:
    import os
    os.system('pip3 install requests')
import json

# 这个 url 从 PC 端钉钉群组->管理机器人里获得
dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=3884f496622bb7ca86bae635726729e4fbef4d5bxxxxxxxxxxxxxxxx"

headers = {"Content-Type": "application/json; charset=utf-8"}

post_data = {
    "msgtype": "text",
    "text": {
        "content": u"运维消息：服务异常"
    },
    "at": {
        "atMobiles": ["188*****021"]
    }
}

r = requests.post(dingding_url, headers=headers,
                  data=json.dumps(post_data))
print(r.content)
