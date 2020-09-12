# django后端

## 常用命令

**新建项目**

> django-admin startproject lenovo

**新建APP**

> django-admin startapp webshop

**更新数据库表和字段**

> python manage.py makemigrations

> python manage.py migrate

**运行服务**

> python manage.py runserver

## Sqlite数据库

创建Model后执行更新数据库表和字段的命令，自动在/lenovo下创建db.sqlite3数据库文件，并新建表

### 查询语句

#### 查询所有

Model.objects.all()

#### 查询过滤

Model.objects.all().filter(id=1)

#### 查询前N个

Model.objects.all().filter(id=1)[:N]

#### 模糊查询

Model.objects.all().filter(Q(name\_\_contains="a")|Q(introduce\_\_contains="b"))

## 常见问题

**报错信息**

'dict' object has no attribute '_meta'

*字典的对象没有分配__meta属性*

**问题**

如果使用了.value("")，则返回的是一个 ValueQuerySet 格式的数据，ValuQuerySet是QuerySet的子类,返回的是一个字典dict并不是一个列表list数据

**方法**

取所有的字段

**源代码**

> commodity = Commodity.objects.all().values('id','name','introduce','img_url','thumb_url','price',)

**修改后**

> commodity = Commodity.objects.all()

------

python3 manage.py runserver 启动服务后，提示

> Quit the server with CTRL-BREAK.

**方法**

`ctrl + c`正常退出