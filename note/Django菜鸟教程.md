# Django模板
1. 模板语法
* 字典传值
* {{}}引用
``
{%if condition%}
contents
{%endif%}
``
``
{%for item in lists [reversed]%}
contents
{% endfor%}
``
``
{% ifequal user currentuser%}
contents
{% endifeuqal%}
``
``
{#这是注释#}
``
2. 过滤器
{{bio|first|upper}} # 第一个字母大写
{{bio|truncatewords:'30'}} # 取前30个字符

3. {%include 'nav.html'%}
# Django模型
* 安装mysql驱动
pip install mysqlclient
* settings.py配置数据库
* 创建App
django-admin startapp TestModel
1. setting.py添加配置 INSTALLED_APPS中添加'TestModel'
# Django 表单
# Django Admin 管理工具
# Django Nginx+uesgi安装配置[Django部署]
# 参考
[](http://www.runoob.com/django/django-first-app.html)