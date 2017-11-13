###ubuntu14.04安装virtualenv
1.先安装pip工具<br>
``apt-get install pip``<br>
2.直接用pip安装virtualenv<br>
``pip install virtualenv``<br>
3.安装virtualenvwrapper,virtualenvwrapper是virtualenv的扩展工具，
可以方便的创建、删除、复制、切换不同的虚拟环境。<br>
``pip install virtualenvwrapper``<br>
4.创建一个文件夹，用于存放所有的虚拟环境：<br>
``mkdir ~/workspaces``<br>
5.在~/.bashrc里添加以下两行<br>
``export WORKON_HOME=~/workspaces``<br>
``source /usr/local/bin/virtualenvwrapper.sh``<br>
6.使配置生效<br>
``source ~/.bashrc``<br>
参考链接:<br>
http://www.linuxidc.com/Linux/2016-04/130196.htm<br>
http://www.xuzefeng.com/post/89.html<br>
http://blog.csdn.net/CV_YOU/article/details/77920945<br>
http://blog.csdn.net/little_nai/article/details/70064604<br>