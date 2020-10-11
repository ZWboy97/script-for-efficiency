try:
    import requests
except ImportError:
    import os
    os.system('pip3 install requests')
import json


def sendMsg(msg, atList=[]):
    # 这个 url 从 PC 端钉钉群组->管理机器人里获得
    dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=3884f496622bb7ca86bae635726729e4fbef4d5beda3e6f739c09e2a29244f39"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    post_data = {
        "msgtype": "text",
        "text": {
            "content": f'运维消息：{msg}'
        },
        "at": {
            "atMobiles": atList
        }
    }
    r = requests.post(dingding_url, headers=headers,
                      data=json.dumps(post_data))
    print(r.content)
