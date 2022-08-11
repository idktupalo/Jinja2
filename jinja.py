from jinja2 import Template

lst = ['a', 'b', 'c', 'd']

temp = '''
	<ul>
	{% for item in data %}
		<li>{{item}}</li>
	{% endfor %}
	</ul> 
'''

tag = Template(temp).render(data = lst)

with open('index.html','w', encoding='utf-8') as file:
	file.write(tag)

