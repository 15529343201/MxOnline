# ubuntu14.04安装virtualenv<br>
### 1.先安装pip工具<br>
``apt-get install pip``<br>
### 2.直接用pip安装virtualenv<br>
``pip install virtualenv``<br>
### 3.安装virtualenvwrapper,virtualenvwrapper是virtualenv的扩展工具，
可以方便的创建、删除、复制、切换不同的虚拟环境。<br>
``pip install virtualenvwrapper``<br>
### 4.创建一个文件夹，用于存放所有的虚拟环境：<br>
``mkdir ~/workspaces``<br>
### 5.在~/.bashrc里添加以下两行<br>
``export WORKON_HOME=~/workspaces``<br>
``source /usr/local/bin/virtualenvwrapper.sh``<br>
### 6.使配置生效<br>
``source ~/.bashrc``<br>
参考链接:<br>
http://www.linuxidc.com/Linux/2016-04/130196.htm<br>
http://www.xuzefeng.com/post/89.html<br>
http://blog.csdn.net/CV_YOU/article/details/77920945<br>
http://blog.csdn.net/little_nai/article/details/70064604<br>
# Django app
users-用户管理<br>
course-课程管理<br>
organization-机构和教师管理<br>
operation-用户操作管理<br>
新建虚拟环境<br>
``mkvirtualenv mxonline``<br>
安装django<br>
``pip install django==1.9``<br>
创建django项目<br>
``django-admin startproject MxOnline``<br>
用pycharm打开后目录结构<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/1.PNG)<br>
添加虚拟环境python解析器<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/2.PNG)<br>
安装mysql<br>
``apt-get install mysql-server``<br>
http://www.linuxidc.com/Linux/2014-05/102366.htm<br>
安装mysql驱动<br>
``pip install mysql-python``<br>
http://blog.csdn.net/wang1144/article/details/50965941<br>
ubuntu安装mysql可视化工具MySQL-workbench<br>
http://blog.csdn.net/jgirl_333/article/details/48575281<br>
创建数据库<br>
``CREATE DATABASE mxonline DEFAULT CHARACTER utf8;``<br>
配置setting<br>
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"mxonline",
        'USER':'root',
        'PASSWORD':"123456",
        'HOST':"127.0.0.1"
    }
}
```
生成django默认表<br>
``python manage.py makemigrations``<br>
``python manage.py migrate``<br>
运行django<br>
``python manage.py runserver``<br>
浏览器显示:<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/3.PNG)

新建users app<br>
``django-admin startapp users``<br>

建立UserProfile model类<br>
```python
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female","女")),default="female")
    address = models.CharField(max_length=100,default=u"")
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username
```		
在setting中注册:<br>
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',
    'users',
]
AUTH_USER_MODEL="users.UserProfile"
```
安装pillow<br>
``pip install pillow``<br>
users表migration<br>
``python manage.py makemigrations``<br>
``python manage.py migrate``<br>

解决各model间循环引用问题<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/4.PNG)<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/5.PNG)<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/6.PNG)<br>
users models.py<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/7.PNG)<br>
完成users models.py编写最终代码:<br>
```python
# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female","女")),default="female")
    address = models.CharField(max_length=100,default=u"")
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u"验证码")
    email=models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type=models.CharField(choices=(("register","注册"),("forget",u"找回密码")),max_length=10)
    send_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u"标题")
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图",max_length=100)
    url=models.URLField(max_length=200,verbose_name=u"访问地址")
    index=models.IntegerField(default=100,verbose_name=u"顺序")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural=verbose_name
```
新建courses app<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/8.PNG)<br>
完成courses models<br>
```python
# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name=u"课程名")
    desc=models.CharField(max_length=300,verbose_name=u"课程描述")
    detail=models.TextField(verbose_name=u"课程详情")
    degree=models.CharField(verbose_name=u"难度",choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=2)
    learn_times=models.IntegerField(default=0,verbose_name=u"学习时长(分钟数)")
    students=models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums=models.IntegerField(default=0,verbose_name=u"收藏人数")
    image=models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面图",max_length=100)
    click_nums=models.IntegerField(default=0,verbose_name=u"点击数")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name=u"课程")
    name=models.CharField(max_length=100,verbose_name=u"章节名")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"章节"
        verbose_name_plural=verbose_name


class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"视频"
        verbose_name_plural=verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name=models.CharField(max_length=100,verbose_name=u"名称")
    download=models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程资源"
        verbose_name_plural=verbose_name
```
新建organization app<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/9.PNG)<br>
完成organization models.py<br>
```python
# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime


from django.db import models


class CityDict(models.Model):
    name=models.CharField(max_length=20,verbose_name=u"城市")
    desc=models.CharField(max_length=200,verbose_name=u"描述")
    add_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"城市"
        verbose_name_plural=verbose_name


class CourseOrg(models.Model):
    name=models.CharField(max_length=50,verbose_name=u"机构名称")
    desc=models.TextField(verbose_name=u"机构描述")
    click_nums=models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums=models.IntegerField(default=0,verbose_name=u"收藏数")
    image=models.ImageField(upload_to="org/%Y/%m",verbose_name=u"封面图",max_length=100)
    address=models.CharField(max_length=150,verbose_name=u"机构地址")
    city=models.ForeignKey(CityDict,verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"课程机构"
        verbose_name_plural=verbose_name


class Teacher(models.Model):
    org=models.ForeignKey(CourseOrg,verbose_name=u"所属机构")
    name=models.CharField(max_length=50,verbose_name=u"教师名")
    work_keys=models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company=models.CharField(max_length=50,verbose_name=u"就职公司")
    work_position=models.CharField(max_length=50,verbose_name=u"公司职位")
    points=models.CharField(max_length=50,verbose_name=u"教学特点")
    click_nums=models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums=models.IntegerField(default=0,verbose_name=u"收藏数")
    add_tiem=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"教师"
        verbose_name_plural=verbose_name
```
新建operation app<br>
![image](https://github.com/15529343201/MxOnline/blob/master/image/11.PNG)<br>
完成operation models.py<br>
```python
# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


#用户咨询
class UserAsk(models.Model):
    name=models.CharField(max_length=20,verbose_name=u"姓名")
    mobile=models.CharField(max_length=11,verbose_name=u"手机")
    course_name=models.CharField(max_length=50,verbose_name=u"课程名")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"用户咨询"
        verbose_name_plural=verbose_name


#课程评论
class CourseComments(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name=u"用户")
    course=models.ForeignKey(Course,verbose_name=u"课程")
    comments=models.CharField(max_length=200,verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程评论"
        verbose_name_plural=verbose_name


#用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id=models.IntegerField(default=0,verbose_name=u"数据id")
    fav_type=models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")),default=1,verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"用户收藏"
        verbose_name_plural=verbose_name


#用户消息
class UserMessage(models.Model):
    user=models.IntegerField(default=0,verbose_name=u"接收用户")
    message=models.CharField(max_length=500,verbose_name=u"消息内容")
    has_read=models.BooleanField(default=False,verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"用户消息"
        verbose_name_plural=verbose_name


#用户课程
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name
```
生成以上app的表

新建python package名为apps
![image](https://github.com/15529343201/MxOnline/blob/master/image/10.PNG)
选中建立的4个app,鼠标拖动到apps中
![image](https://github.com/15529343201/MxOnline/blob/master/image/12.PNG)
![image](https://github.com/15529343201/MxOnline/blob/master/image/13.PNG)
把apps加入到python的搜索路径之下：
```python
import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
```