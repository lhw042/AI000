我 python2 和 python3 的路径是不一样的
python2`/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload`
ipython 的路径`/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages`
而我 python3 的路径却在`Applications`里
pip3` /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages`
pip`/Library/Python/2.7/site-packages`
requests`/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages`
也就是说大部分的库都是在 libray 中的 
当我重新安装完后，命令行提示我安装成功，但是输入 virtualenv --help  `-bash: virtualenv: command not found`.未找到命令，再来找一下这个刚下载的文件在哪里

