#step06_tuple.py

'''
    -tuple
    1. list type과 유사
    2. 읽기 전용 (수정, 삭제 불가)
    3. 기능이 적기 때문에 처리속도가 빠르다

    만드는 방법
    (value1, value2, value3)
'''

tuple : tuple = ("one","two","three")

result1 = tuple[0]
result2 = tuple[1]
result3 = tuple[2]

# readonly 이기 때문에 수정,삭제가 불가하다
#del tuple[0]
#tuple1.remove(0)
#tuple[0] = 'xxx'

# 방 1개 짜리 tuple type 을 만들 때는 주의, 끝에 ,를 붙혀줘야함
tuple2 = ("최진혁" ,)

# 괄호 없는 튜플 생성
tuple3 = 10,20,30

#tuple 에 저장된 값을 여러 변수에 나누어 담기
a,b,c = tuple3

# 두 변수에 있는 값을 서로 바꾸려면?
first = "girl"
second = "boy"

# 우측의 tuple 값을 first, second 변수에 각각 담기
first, second = second, first

print("종료")