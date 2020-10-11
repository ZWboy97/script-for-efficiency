import http_request
from threading import Timer
import time
import dingmsg

last_msg_time = time.time()


def test_streams_status(test_streams_list=[]):
    data1 = http_request.get('http://1xx.xx.x.164:1985/api/v1/streams/')
    data2 = http_request.get('http://1xx.xx.x.165:1985/api/v1/streams/')
    app_stream_list = []
    if data1 != None:
        if data1.__contains__('streams'):
            streams = data1['streams']
            for stream in streams:
                app = stream['app']
                name = stream['name']
                app_stream_list.append(f'h1/{app}/{name}')
    if data2 != None:
        if data2.__contains__('streams'):
            streams = data2['streams']
            for stream in streams:
                app = stream['app']
                name = stream['name']
                app_stream_list.append(f'h2/{app}/{name}')
    err_streams = []
    for stream in test_streams_list:
        if stream in app_stream_list:
            continue
        else:
            err_streams.append(stream)
    print(f'err count = {len(err_streams)}')
    if len(err_streams) > 0:
        global last_msg_time
        curr_time = time.time()
        t = curr_time - last_msg_time
        err_msg = ""
        for stream in err_streams:
            err_msg += f',{stream}'
        # 限制5分钟内发送一次错误消息
        if t > 300:
            dingmsg.sendMsg(
                f'检测到有流不存在，它们是 {err_msg}，5分钟后我会再通知', ['18811798021'])
            last_msg_time = time.time()

    return err_streams


def start_time_task(test_streams_list):
    test_streams_status(test_streams_list)
    # 60 秒执行一次
    sTimer = Timer(3, start_time_task, args=[test_streams_list])
    sTimer.start()
    # sTimer.join() 等待定时器结束


test_streams_list = ['h2/live/zjn', 'h2/xr/live', 'h1/live/test']

start_time_task(test_streams_list)
