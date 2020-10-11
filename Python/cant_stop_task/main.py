import run


def start_all_task():
    # 启动SRS
    srs_start_script = "cd /developer/srs/trunk/ && ./objs/srs -c conf/hls_flv.conf"
    run.runCmdWithRetry(srs_start_script, "主SRS服务")

    # 启动全景原始拉流
    pull_pano_video = "ffmpeg "
    run.runCmdWithRetry(pull_pano_video, "全景原视拉流")

    # 启动全景转码推流
    push_transcode_pano_video = "ffmpeg "
    run.runCmdWithRetry(push_transcode_pano_video, "全景转码推流")

    # 启动无人车拉流
    pull_car_video = "ffmpeg "
    run.runCmdWithRetry(pull_pano_video, "无人车原视拉流+转码")
