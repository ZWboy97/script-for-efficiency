import subprocess
import dingmsg
import time


def redStr(str):
    return ' \033[1;31m '+str+' \033[0m '


def greenStr(str):
    return ' \033[1;32m ' + str + ' \033[0m '


def yelloStr(str):
    return ' \033[1;33m ' + str + ' \033[0m '


def buleStr(str):
    return ' \033[1;34m ' + str + ' \033[0m '


def runCmdWithRetry(command, task_name, try_count=0, last_run_time=time.time(), duration=1800, errmsg=""):
    # 稳定运行30分钟以上，则撤销报警计数
    slot = time.time() - last_run_time
    if slot > duration:
        try_count = 0
    # 连续重启次数超过5次，则钉钉通知
    if try_count == 5:
        dingmsg.sendMsg(
            f'Task-{task_name}：最近30分钟内异常重启次数达5次，服务已停止，请检查日志。\n错误信息:{errmsg}', ['18811798021'])
        return
    # 更新 last_run_time
    last_run_time = time.time()
    print(buleStr('[Runing]:'+command))
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    outs, errs = subp.communicate()
    if subp.poll() == 0:
        print(outs.decode(encoding='UTF-8', errors='null'))
        print(greenStr('[Success]: ' + command))
    else:
        errmsg = errs.decode(encoding='UTF-8', errors='null')
        print(errmsg)
        print(redStr('[Failed]:' + command))
    print(buleStr('running again'))
    try_count = try_count + 1
    runCmdWithRetry(command, task_name, try_count,
                    last_run_time, duration, errmsg)


def runCmd(command):
    print(buleStr('[Runing]:'+command))
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    res = subp.communicate()
    if subp.poll() == 0:
        print(res[0])
        print(greenStr('[Success]: ' + command))
        return 0
    else:
        print(res[0])
        print(redStr('[Failed]:'+command))
        return -1
