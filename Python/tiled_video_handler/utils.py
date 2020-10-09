import os


def create_dir(path):
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    isExists = os.path.exists(path)
    if not isExists:
        return True
    else:
        return False


def get_dirs_in_path(root_dir):
    dir_list = []
    isExists = os.path.exists(root_dir)
    if isExists == False:
        return dir_list
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            dir_list.append(os.path.join(dirpath, dirname))
        break
    return dir_list

# 获取当前路径下的文件，返回文件全路径


def get_files_in_path(root_dir):
    files_list = []
    isExists = os.path.exists(root_dir)
    if isExists == False:
        return files_list
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            files_list.append(filename)
        break
    return files_list


# 获取当前路径下的文件，返回文件全路径
def get_files_path_in_path(root_dir):
    files_list = []
    isExists = os.path.exists(root_dir)
    if isExists == False:
        return files_list
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            files_list.append(os.path.join(dirpath, filename))
        break
    return files_list
