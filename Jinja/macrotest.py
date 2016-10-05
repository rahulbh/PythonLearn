
from jinja2 import Template
t=Template('''
{% macro gen_list_item(item) %}
    <li>{{ item }}</li>
{% endmacro %}
<ul>
  {% for message in messages %}
    {{ gen_list_item(message) }}
  {% endfor %}
</ul>''')

print(t.render(messages=['lol','what','are']))