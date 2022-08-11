from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": 'John', "old": 18, "weight": 60.5},
    {"name": 'Randy', "old": 19, "weight": 65.5},
    {"name": 'Seth', "old": 20, "weight": 70.5},
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

temp = env.get_template('main.html').render(users=persons)  # Template
print(temp)
# from jinja2 import Template
#
# cars_list = [
#     {'model': 'audi', 'id': 1, 'price': 23_000},
#     {'model': 'bmw', 'id': 2, 'price': 25_000},
#     {'model': 'mercedes', 'id': 3, 'price': 27_000},
#     {'model': 'renault', 'id': 4, 'price': 29_000},
# ]
#
# data = Template(temp).render(cars=cars_list)
#
# try:
#     with open('index.html', 'w', encoding='utf-8') as file_html:
#         print(data)
#         file_html.write(data)
# except ValueError:
#     print("Bad news , data don't load(((")


# FILTER
# temp = '<h1>Max items is {{ (crs | max(attribute="price")).model }}</h1>'
# Output: <h1>Max items is renault</h1>
# temp = '<h1>Min item is {{ (crs | min(attribute="price")) }}</h1>'
# Output:<h1>{'model': 'audi', 'price': 23000}</h1>
# temp = '<h1>Sum {{ (crs | sum(attribute="price")) }}</h1>'
# Output:<h1>Sum 104000</h1>
# --------------------------------------------------------------------------------------------
# temp = '''
# {%- for item in crs -%}
# {% filter upper %}{{item.model}}{% endfilter %}
# {% endfor -%}
# '''
# Output: AUDI BMW MERCEDES RENAULT
# --------------------------------------------------------------------------------------------
# MACROS
# temp = '''
# {%- macro input(name, value='', type='text', size = 20) -%}
#     <input type = '{{type}}' , name = '{{name}}', value = '{{value|e}}', size = '{{size}}'>
# {%- endmacro %}
# <p>{{input('username')}}
# <p>{{input('email')}}
# <p>{{input('password', type='password')}}
# '''
# Output:
# <p><input type = 'text' , name = 'username', value = '', size = '20'>
# <p><input type = 'text' , name = 'email', value = '', size = '20'>
# <p><input type = 'password' , name = 'password', value = '', size = '20'>
# --------------------------------------------------------------------------------------------
# CALL
# temp = '''
# {% macro list_cars(list_of_cars) -%}
# <ul>
# {% for car in list_of_cars -%}
#     <li>{{car.model}}{{caller(car)}}</li>
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {% call(cr) list_cars(cars) %}
#     <ul>
#         <li>id:{{cr.id}}</li>
#         <li>cost:{{cr.price}}</li>
#     </ul>
# {% endcall -%}
# '''
#
# Output :
# <ul>
# <li>audi
#     <ul>
#         <li>id:1</li>
#         <li>cost:23000</li>
#     </ul>
# </li><li>bmw
#     <ul>
#         <li>id:2</li>
#         <li>cost:25000</li>
#     </ul>
# </li><li>mercedes
#     <ul>
#         <li>id:3</li>
#         <li>cost:27000</li>
#     </ul>
# </li><li>renault
#     <ul>
#         <li>id:4</li>
#         <li>cost:29000</li>
#     </ul>
# </li>
# </ul>