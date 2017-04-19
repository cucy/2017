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
