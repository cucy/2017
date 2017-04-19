# 模板
## 简单使用样例
```python
In [1]: from django.template import Template, Context

In [2]: import datetime

# 定义模板 占位符
In [3]: raw_template = """<p>Dear {{ person_name }},</p>
   ...: <p>Thanks for placing an order from {{ company }}. It's scheduled to
   ...: ship on {{ ship_date|date:"F j, Y" }}.</p>
   ...: {% if ordered_warranty %}
   ...: <p>Your warranty information will be included in the packaging.</p>
   ...: {% else %}
   ...: <p>You didn't order a warranty, so you're on your own when
   ...: the products inevitably stop working.</p>
   ...: {% endif %}
   ...:
   ...: <p>Sincerely,<br />{{ company }}</p>"""

In [4]: t = Template(raw_template)

# 传入数据
In [5]: c = Context({'person_name': 'John Smith',
   ...:  'company': 'Outdoor Equipment',
   ...:  'ship_date': datetime.date(2015, 7, 2),
   ...:  'ordered_warranty': False})

# 渲染数据
In [6]:   t.render(c)
Out[6]: u"<p>Dear John Smith,</p>\n<p>Thanks for placing an order from Outdoor Equipment. It's scheduled to\nship on July 2, 2015.</p>\n\n<p>You didn't order a warranty, so you're on your own when\nthe products inevitably stop working.</p>\n\n\n<p>Sincerely,<br />Outdoor Equipment</p>"

```
## 模板标签
- if/else
```python
{% if athlete_list %}
   Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
   <p>Athletes should be out of the locker room soon! </p>
{% elif ...  %}
...
{% else %}
<p>No athletes. </p>
{% endif %}
```
- for
```python
<ul>
    {% for athlete in athlete_list %}
        <li>{{ athlete.name }}</li>
    {% endfor %}
</ul>

{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}

{% if athlete_list %}
    {% for athlete in athlete_list %}
        <p>{{ athlete.name }}</p>
    {% endfor %}
{% else %}
    <p>There are no athletes. Only computer programmers.</p>
{% endif %}

# 当对象为空时
{% for athlete in athlete_list %}
    <p>{{ athlete.name }}</p>
{% empty %}
    <p>There are no athletes. Only computer programmers.</p>
{% endfor %}
```
- ifequal/ifnotequal
```python
{% ifequal user currentuser %}
   <h1>Welcome!</h1>
{% endifequal %}

{% ifequal variable True %}
{% ifequal variable [1, 2, 3] %}
{% ifequal variable {'key': 'value'} %}
```
- Comments
```python
{% comment %}
   This is a
   multi-line comment.
{% endcomment %}
```
- Filters 过滤器
```python
{{ name|lower }}

{{ my_list|first|upper }}

{{ bio|truncatewords:"30" }}

{{ pub_date|date:"F j, Y" }}
```

## render()
views.py
```python
# -- coding: utf-8 --
# Time: 2017/4/19 14:44
# Author: zhourudong
from django.shortcuts import render
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html',
                  {'current_date': now})
```
templates/
- 基础模板
base.html
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
```
- current_datetime.html
```html
<h1>My helpful timestamp site</h1>
{% block content %}

{% endblock %}
{% block footer %}
    <hr>
    <p>Thanks for visiting my site.</p>
{% endblock %}
</body>
</html>
```

# 模型
- 定义使用的数据库
settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

- 模型基本状况
```
作者
	姓名
	邮箱地址
出版社
	出版社名
	街道地址
	城市
	国家
	网址
书
	书名
	发布日期
	作者（多对多）
	发版商（一对多)
```
models.py
```python
# coding:utf8
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'发版商')
    address = models.CharField(max_length=50, verbose_name=u'地址')
    city = models.CharField(max_length=60, verbose_name=u'城市')
    state_province = models.CharField(max_length=30, verbose_name=u'街道')
    country = models.CharField(max_length=50, verbose_name=u'国家')
    website = models.URLField(verbose_name=u'网址')


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=u'姓')
    last_name = models.CharField(max_length=40, verbose_name=u'名')
    email = models.EmailField(verbose_name=u'邮箱地址')


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'书名')
    authors = models.ManyToManyField(Author, verbose_name=u'作者') #多对多
    publisher = models.ForeignKey(Publisher, verbose_name=u'发版商') #  一对多
    publication_date = models.DateField(verbose_name=u'发布日期')
```
- 生成数据库迁移文件
```python
python manage.py makemigrations books
```
- 查看生成的sql
```sql
$ python manage.py sqlmigrate books 0001
BEGIN;
CREATE TABLE "books_author" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "last_name" varchar(40) NOT NULL, "email" varchar(254) NOT NULL);
CREATE TABLE "books_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "publication_date" date NOT NULL);
CREATE TABLE "books_book_authors" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "book_id" integer NOT NULL REFERENCES "books_book" ("id"), "author_id" integer NOT NULL REFERENCES "books_author" ("id"), UNIQUE ("book_id", "author_id"));
CREATE TABLE "books_publisher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL, "address" varchar(50) NOT NULL, "city" varchar(60) NOT NULL, "state_province" varchar(30) NOT NULL, "country" varchar(50) NOT NULL, "website" varchar(200) NOT NULL);
CREATE TABLE "books_book__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "publication_date" date NOT NULL, "publisher_id" integer NOT NULL REFERENCES "books_publisher" ("id"));
INSERT INTO "books_book__new" ("publication_date", "publisher_id", "id", "title") SELECT "publication_date", NULL, "id", "title" FROM "books_book";
DROP TABLE "books_book";
ALTER TABLE "books_book__new" RENAME TO "books_book";
CREATE INDEX "books_book_2604cbea" ON "books_book" ("publisher_id");

COMMIT;
```
- 同步数据库
```python
python manage.py migrate
```
## 基础查询
```python
In [1]: from books.models import Publisher

In [2]: p1 = Publisher(name='清华出版社', address='2855 Telegraph Avenue',
   ...: city='北京', state_province='CA', country='CN',
   ...: website='http://www.qinghua.com/')

In [3]: p1.save()
In [4]: p2 = Publisher(name="图灵出版社", address='10 Fawcett St.',
   ...: city='Cambridge', state_province='MA', country='U.S.A.',
   ...: website='http://www.oreilly.com/')

In [5]: p2.save()
# 另一种创建方法
>>> p1 = Publisher.objects.create(name='Apress',
 address='2855 Telegraph Avenue',
 city='Berkeley', state_province='CA', country='U.S.A.',
 website='http://www.apress.com/')
>>> p2 = Publisher.objects.create(name="O'Reilly",
 address='10 Fawcett St.', city='Cambridge',
 state_province='MA', country='U.S.A.',
 website='http://www.oreilly.com/')
>>> publisher_list = Publisher.objects.all()
>>> publisher_list
[<Publisher: Publisher object>, <Publisher: Publisher object>]

# 查询
```
