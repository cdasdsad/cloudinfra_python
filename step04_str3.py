# yaml 문자열을 다룰때는 외부 모듈을 pip로 설치를 해서 import 를 해야한다.
# python 가상환경을 구성하고 pip install pyyaml 설치 후에 yaml을 다룰 수 있다.

import yaml
# yaml 형식의 문자열 작성해보기

info = '''
    name : 최진혁
    addr : 창원
    foods :
      - 맥주
      - 베이컨
    isMan : True
    body :
      weight : 75
      height : 174
'''

# yaml 형식의 문자열을 로딩해서 dict type 으로 변경하기
result = yaml.safe_load(info)
print(result)

print("------------------------------")
# dict tupe 을 다시 yaml 형식의 문자열로 변환하기
# allow_unicode=True 한글 알아볼 수 있게함
result2 = yaml.dump(result, allow_unicode=True, sort_keys=False)

print(result2)