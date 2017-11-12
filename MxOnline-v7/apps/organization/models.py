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

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name=models.CharField(max_length=50,verbose_name=u"机构名称")
    desc=models.TextField(verbose_name=u"机构描述")
    category=models.CharField(default="pxjg",verbose_name=u"机构类别",max_length=20,choices=(("pxjg","培训机构"),("gr","个人"),("gx","高校")))
    click_nums=models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums=models.IntegerField(default=0,verbose_name=u"收藏数")
    image=models.ImageField(upload_to="org/%Y/%m",verbose_name=u"logo",max_length=100)
    address=models.CharField(max_length=150,verbose_name=u"机构地址")
    city=models.ForeignKey(CityDict,verbose_name=u"所在城市")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0,verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now)
    '''
    增加一个字段:
    alter table table_name add column(字段名 字段类型)
    指定字段插入的位置：
    alter table table_name add column 字段名 字段类型 after 某字段
    删除一个字段:
    alter table table_name drop 字段名
    '''

    class Meta:
        verbose_name=u"课程机构"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name

    def get_teacher_nums(self):
        #获取课程机构的教师数
        return self.teacher_set.all().count()



class Teacher(models.Model):
    org=models.ForeignKey(CourseOrg,verbose_name=u"所属机构")
    name=models.CharField(max_length=50,verbose_name=u"教师名")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company=models.CharField(max_length=50,verbose_name=u"就职公司")
    work_position=models.CharField(max_length=50,verbose_name=u"公司职位")
    points=models.CharField(max_length=50,verbose_name=u"教学特点")
    click_nums=models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums=models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name=u"头像", max_length=100)
    add_tiem=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"教师"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.all().count()