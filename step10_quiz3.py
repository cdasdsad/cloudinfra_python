from jinja2 import Template

posts = [
    {"id" : 1, "writer" : "작성자1", "title" : "제목1"},
    {"id" : 2, "writer" : "작성자2", "title" : "제목2"},
    {"id" : 3, "writer" : "작성자3", "title" : "제목3"}
]

sample = '''
    {%- for i in posts %}
        - 글번호 : {{i.id}} 작성자 : {{i.writer}} 제목 : {{i.title}}
    {%- endfor %}
'''

t1 = Template(sample)
result = t1.render(posts = posts)
print(result)