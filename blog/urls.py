# _*_ coding:UTF-8 _*_
# path:/home/tarena/桌面/study_file/...

"""
作者：朱文涛
邮箱：wtzhu_13@163.com

时间：2019/05
描述：
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 博客内容显示页面链接：127.0.0.1:8000/blog/
    url(r'^$', views.archive),
    # 博客内容提交页面链接：127.0.0.1:8000/blog/create/
    url(r'^create/$', views.create_blog),

]
