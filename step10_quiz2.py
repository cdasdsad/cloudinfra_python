from jinja2 import Template

info = {
    "num" :1,
    "name" : "김구라",
    "body" : {
        "height" : 180,
        "weight" : 80
    },
    "hobby" : ["피아노","당구","프로그래밍"]
}

sample = '''
    번호 : {{ num }}
    이름 : {{ name }}
    키 : {{ body.height }} cm
    몸무게 : {{ body.weight }} kg
    취미 :
    {%- for i in hobby %}
       - {{ i }}
    {%- endfor %}
'''

t1 = Template(sample)
result = t1.render(info)
print(result)