import sys
import pickle
import re
import codecs
import string
import shutil
from win32com import client as wc
import docx
import os
import os.path

# 修改参数
workspace_dir = "W:\\WorkPlace\\Python\\word_handler\\"  # 批处理文件所在的目录


def get_doc_file_list(dir_path):
    file_list = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.endswith('.doc'):
                file_list.append(filename)
    return file_list


def change_doc_to_docx(doc_file_name):
    print('\n当前处理文件：' + str(workspace_dir + doc_file_name))
    word = wc.Dispatch('Word.Application')
    word.Visible = True
    doc = word.Documents.Open(workspace_dir + doc_file_name)  # 目标路径下的文件
    new_file_name = doc_file_name.replace(".doc", ".docx")
    doc.SaveAs(workspace_dir + new_file_name, 12, False, "", True,
               "", False, False, False, False)  # 转化后路径下的文件
    doc.Close()
    word.Quit()
    print('处理成功，另存为新文件，新文件路径：'+str(workspace_dir+new_file_name))
    return


def main():
    doc_file_list = get_doc_file_list(workspace_dir)
    print('There are ' + str(len(doc_file_list)) +
          " doc files in " + str(workspace_dir))
    for file_name in doc_file_list:
        change_doc_to_docx(file_name)
    print('\n处理完毕！')
    return


main()
