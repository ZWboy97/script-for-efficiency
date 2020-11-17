import cmder
import utils

video_output_dir = "W:\\WorkPlace\\script-for-efficiency\\Python\\tiled_video_handler\\output\\1-1\\"


def dash_all_videos(video_output_dir):
    dirs = utils.get_dirs_path_in_path(video_output_dir)
    for dirpath in dirs:
        print(dirpath)
        cmder.runCmd(
            f'mp4box -dash 1000 -rap -profile dashavc264:onDemand L0.mp4#video L1.mp4#video L0.mp4#audio')


dash_all_videos(video_output_dir)
