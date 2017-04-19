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
