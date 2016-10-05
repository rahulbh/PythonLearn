# -*- coding: UTF-8 -*-
from jinja2 import Template
t = Template('''
<ul>
{% for item in items %}<li>
  {% if loop.first %}THIS IS ITEM 1{% endif %}
  {{ loop.index }}: {{ item }} ({{ loop.cycle('odd', 'even') }})</li>
{% endfor %}
</ul>''')

print(t.render(items=['apple', 'banana', 'cherry']))