# django web框架项目
## Django 2.0 新URL配置
[](https://www.cnblogs.com/feixuelove1009/p/8399338.html)
``
urlpatterns=[
   path('articles/2003/',view.special_case_2003),
   path('articles/<int:year>/',view.year), # view.year(request,year)
]
``
# 经验值
1. 工程建立后将工程名大写，防止产生包冲突
# 开发计划
* 菜鸟教程
* 后端完成
# 相关命令
##  安装
pip install django
## 创建一个项目
django-admin startproject HelloWorld
## 启动项目
python manage.py runserver 127.0.0.1:8000
## 快速配置billing
1. 安装anaconda
2. 依赖django
3. 启动python manage.py runserver 127.0.0.1:8000