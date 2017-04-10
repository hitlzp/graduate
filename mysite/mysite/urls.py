"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('', url(r'^admin/', include(admin.site.urls)), \
                        url(r'^$', 'student.views.menu'), \
                        url(r'^test/$', 'student.views.ajax_course'), \
                        url(r'^test2/$', 'student.views.ajax_segment'), \
                        url(r'^test3/$', 'student.views.ajax_finally'), \
                        url(r'^teacher/course/mycourse/$', 'student.views.editcourse'), \
                        url(r'^teacher/course/mycourse/ajax/$', 'student.views.editcourse_ajax'), \
                        url(r'^student/$', 'student.views.login_s'), \
                        url(r'^teacher/$', 'student.views.login_t'), \
                        url(r'^logout/$', 'student.views.logout'), \
                        url(r'^student/reg/$', 'student.views.reg_s'), \
                        url(r'^teacher/reg/$', 'student.views.reg_t'), \
                        url(r'^forgot/$', 'student.views.forgot'), \
                        url(r'^student/main/$', 'student.views.studentmain'), \
                        url(r'^teacher/main/$', 'student.views.teachermain'), \
                        url(r'^teacher/coursemanage/$', 'student.views.coursemanage'), \
                        url(r'^teacher/addcourse/$', 'student.views.addcourse'), \
                        url(r'^teacher/addcourse/addsegment/$', 'student.views.addsegment'), \
                        url(r'^teacher/addcourse/finally/$', 'student.views.addfinally'), \
                        url(r'^teacher/class/$', 'student.views.inclass'), \
                        url(r'^teacher/classajax/$', 'student.views.inclassajax'), \
                        url(r'^teacher/fenzu/$', 'student.views.Fenzu'), \
                        url(r'^teacher/randstu/$', 'student.views.Randstu'), \
                        url(r'^teacher/randgroup/$', 'student.views.Randgroup'), \
                        url(r'^student/mycourse/$', 'student.views.Mycourse'), \
                        url(r'^student/mycourseajax/$', 'student.views.Mycourseajax'), \
                        )