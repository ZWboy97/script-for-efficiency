# 用于从大量的.doc中提取有用的信息，这些信息在word表格中


## 一、安装环境
1. 安装python3，需要使用python3，python2没测试过
2. 安装pip3

## 二、安装包和依赖
1. 安装xlwt
```
pip3 install xlwt
```
2. 安装 pypiwin32
```
pip3 install pypiwin32
```
3. 安装python-docx
```
pip3 install python-docx
```

## 三、使用步骤
1. 使用pre_handler.py将.doc文件批量处理为.docx文件
- 电脑上需要安装微软的Word程序
- 修改pre_handler.py中第13行的workspace_dir为文件所在的目录
- 启动执行：
```
python3 pre_handler.py
```
2. 使用main.py从处理之后的.docx文件中提取信息，并存储到excel中
- 修改main.py中第8行的workspace_dir为文件所在的目录
- 启动执行：
```
python3 main.py
```
