import json

#json 형식의 문자열을 작성하고 python에서 활용해보자
info = '''
    {
        "name" :"최진혁",
        "addr" : "창원",
        "foods" : ["맥주","베이컨"]
    }
'''

result = json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

result2 = json.dumps(result)

print("종료")
