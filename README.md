# 积累一些日常用到的脚本效率工具

- 作为技术人，要想方设法的来提高效率。

## Python
- word_handler: 通过python语言来批量从多个word文档中提取信息，并导出到Excel中。
    - 批量.doc转.docx
    - Word中读取表格信息
- [tiled_video_handler](./Python/tiled_video_handler/README.md)：用于全景视频的分块传输，实现将全视角的全景视频切分成多个tile，并将每个tile生成多个不同质量的版本，并以Dash进行自适应传输
    - 批量对多个视频进行crop切割和加文字水印操作
    - 批量对多个视频进行多码率转换
    - 批量对多个视频进行Dash切片
    - 批量对多组Dash切片生成.mpd文件

- [cant_stop_task](./Python/cant_stop_task/README.md): python编写的自动重启脚本，同时配置了钉钉机器人，及时通知报警信息到钉钉群
    - 使用python执行命令行，启动服务
    - 服务异常退出时，自动重试
    - 服务异常通过钉钉机器人，发送到钉钉群组
    
## Shell
- [oh_my zsh_installer](./Shell/install-zsh/README.md): 一个顺手的命令行环境能有效提升效率，解决新服务器如何快速配置oh-my-zsh的问题
    - 脚本安装oh-my-zsh
    - 配置oh-my-zsh主题
