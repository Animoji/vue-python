# 这是一个Vue+Python的项目

* vue为前端框架

* python作为后端处理语言

* 其中vue使用了[element-ui](http://element.eleme.io/#/zh-CN)组件库

* python使用django框架,如何使用请参考：<br>
	[django使用教程](http://www.runoob.com/django/django-tutorial.html)

* 此项目实现了前后端分离



# vue配置

## Build Setup

``` bash
# 安装依赖
npm install

# 安装webpack-dev-server
npm install -g webpack-dev-server

# 服务将会监听localhost:8080
npm run dev

# 最小化方式编译
npm run build

# 编译为生产环境并查看分析报告
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).




# python配置

## 本项目使用的python版本为Python 3.x，添加的包如下：<br>

* Django 2.1a1

* demjson 2.2.4

* django-cors-headers 2.2.0

* django-json-response 1.1.5

* mysqlclient 1.3.12

* pip 10.0.1

* pytz 2018.4

* setuptools 39.2.0

## 数据库相关配置请参阅：<br>
	[Django模型](http://www.runoob.com/django/django-model.html)

## 安装依赖后，请输入以下命令创建相应数据库：

``` bash
python manage.py makemigrations myapp

python manage.py migrate
```