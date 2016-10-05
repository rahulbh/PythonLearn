from jinja2 import Template
t1 = Template('Hello, {{ name|striptags }}')
x=t1.render(name='<em>Peter</em>')
print(x)