import cmder
import os
import os.path

workspace_dir = "W:\\WorkPlace\\script-for-efficiency\\Python\\tiled_video_handler\\videos\\"  # 批处理文件所在的目录
video_src_dir = workspace_dir
video_output_dir = "W:\\WorkPlace\\script-for-efficiency\\Python\\tiled_video_handler\\output\\"

TILE_WIDTH = 640
TILE_HEIGHT = 480


def get_video_list(dir_path):
    video_list = []
    for parent, dirname, filenames in os.walk(dir_path):
        for filename in filenames:
            video_list.append(filename)
    return video_list


def create_output_dir(dir_path, file_name):
    path = dir_path + file_name
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    isExists = os.path.exists(path)
    if not isExists:
        return True
    else:
        return False


def crop(video_path, width, height, x, y, output_path, mark):
    res = cmder.runCmd(
        f'ffmpeg -i {video_path} -vf crop={width}:{height}:{x}:{y},drawtext=fontcolor=white:fontsize=40:text=\'{mark}\':x=10:y=10 {output_path} -y')
    if res == -1:
        os._exit(-1)


def crop_video(video_dir, name, output_dir):
    for i in range(0, 4):
        for j in range(0, 3):
            x = TILE_WIDTH * i
            y = TILE_HEIGHT * j
            dir_name = name+"\\"+"tile_"+str(i)+"_"+str(j)+"\\"
            res = create_output_dir(output_dir, dir_name)
            output_path = output_dir + dir_name + "L0.mp4"
            crop(video_dir+name, TILE_WIDTH, TILE_HEIGHT,
                 x, y, output_path, f'Tile({i}-{j})-L0')


def start_crop_videos(video_dir, output_dir):
    video_src_dir = video_dir
    video_output_dir = output_dir
    videoNames = get_video_list(workspace_dir)
    print("There are " + str(len(videoNames)) + " videos in this path")
    if (len(videoNames) == 0):
        print(cmder.redStr("ERROR: Not found video files"))
        return
    for name in videoNames:
        print("Crop " + video_dir + name)
        crop_video(video_dir, name, output_dir)


start_crop_videos(video_src_dir, video_output_dir)
