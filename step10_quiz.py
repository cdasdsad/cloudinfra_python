from jinja2 import Template

data = ["김구라", "해골", "원숭이"]

sample = '''
<ul>
    {%- for name in names %}
        <li> {{ name }} </li>
    {%- endfor %}
</ul>
'''

t1 = Template(sample)
result = t1.render(names = data)
print(result)

print("----------------------------------------")

data2 = ["주뎅이","덩어리","개다리"]
result2 = t1.render(names = data2)
print(result2)