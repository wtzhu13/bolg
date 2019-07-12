# django简易博客demo

## 简介
通过django矿建搭建一个简易的博客项目，实现编写博文，提交并显示的功能
内容按照发表时间济宁排序，最新的发布排在前面。该demo可以熟悉django框
架的基本操作。

## 所需环境及配置
1. Python版本 3.7.3
2. MySQL ： 5.7.26-0ubuntu0.18.04.1
3. django : 2.2.3

## 操作指引
1. 根据数据库的账号密码修改setting.py的配置。
2. 根据setting.py中数据库名创建数据库。
3. 在 manage.py 目录下通过一下命令进行数据库迁移
    ```python3 mamage.py makemigrations```
    ```python3 mamage.py migrate```
    迁移完成后数据库中会自动生成对应表。
4. 在 manage.py 目录下通过一下命令运行
    ```python3 mamage.py runserver```
5. 通过```python3 manage.py createsuperuser```创建超级用户
   然后在127.0.0.1:8000/admin中从后台管理数据。

## 主要思路
通过主路由中的URL定位到app中的URL，然后根据app中的URL定位到app的视图
函数中具体的函数，然后在函数中对数据进行操作。

## 表管理
主要是创建了博客内容表，字段为title保存博客标题，body保存博客内容，timestamp保存创建时间。








