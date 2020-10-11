try:
    import requests
except ImportError:
    import os
    os.system('pip3 install requests')
import json


def get(url):
    # 这个 url 从 PC 端钉钉群组->管理机器人里获得
    headers = {"Content-Type": "application/json; charset=utf-8"}
    r = requests.get(url, headers=headers)
    data = r.json()
    return data
