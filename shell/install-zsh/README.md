# 安装Oh My Zsh

## 1 安装 zsh

```bash
apt install zsh
```

## 2. 脚本安装 oh my zsh

```
chmod 777 ./install.zsh
./install-zsh.sh
```

## 3. 配置 oh my zsh
```bash
# 配置文件位于 ~./zshrc
ZSH_THEME="agnoster" # 配置主题，将名字换掉就可 https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
plugins=(git) # 配置插件，多了启动会慢
```