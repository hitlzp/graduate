# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
 
class User_class(models.Model):
    person = models.ForeignKey(User)
    clas = models.IntegerField(verbose_name='身份类别', default=0)
    
class Course_t(models.Model):
    teacher = models.ForeignKey(User)
    cname = models.CharField(max_length=100)
    sum= models.IntegerField(default=0)
    recommend = models.TextField()
    segmentsum  = models.IntegerField(default=0)
    groupsum = models.IntegerField(default=0)
    starttime = models.DateTimeField(default = "2017-01-01 00:00:00")
    isvalid = models.IntegerField(default=0)
    mytype = models.IntegerField(default=0)
    
class Segmnet_t(models.Model):
    tcourse = models.ForeignKey(Course_t)
    sname = models.CharField('环节名称',max_length=100)
    minute = models.IntegerField(default=0)
    content = models.TextField()
    ratio = models.IntegerField(default=0)
    isvalid = models.IntegerField(default=0)
    
class Table_t(models.Model):
    tsegment = models.ForeignKey(Segmnet_t)
    choice = models.IntegerField(default=0)
    ratio = models.IntegerField(default=0)
    
class Students(models.Model):
    stu = models.ForeignKey(User)
    course = models.ForeignKey(Course_t)
    group = models.IntegerField(default=0)
    grade = models.FloatField(default=0)