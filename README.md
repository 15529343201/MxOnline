###ubuntu14.04安装virtualenv
1.先安装pip工具
``apt-get install pip``
2.直接用pip安装virtualenv
``pip install virtualenv``
3.安装virtualenvwrapper,virtualenvwrapper是virtualenv的扩展工具，
可以方便的创建、删除、复制、切换不同的虚拟环境。
``pip install virtualenvwrapper``
4.创建一个文件夹，用于存放所有的虚拟环境：
``mkdir ~/workspaces``
5.在~/.bashrc里添加以下两行
``export WORKON_HOME=~/workspaces
source /usr/local/bin/virtualenvwrapper.sh``
6.使配置生效
``source ~/.bashrc``
参考链接:
http://www.linuxidc.com/Linux/2016-04/130196.htm
http://www.xuzefeng.com/post/89.html
http://blog.csdn.net/CV_YOU/article/details/77920945
http://blog.csdn.net/little_nai/article/details/70064604