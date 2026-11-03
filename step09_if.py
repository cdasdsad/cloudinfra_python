#step09_if.py

'''
    임의의 숫자를 입력 받아서 입력한 수가 양수 이면 "양수 입니다."를
    출력 하고자 한다면???\
    
    (if문 필요)
'''

input_num : int = int(input("임의의 숫자입력:"))

if(input_num > 0) :
    print(f"입력한 숫자는 {input_num} 은 앙수 입니다")
elif(input_num < 0) :
    print(f"입력한 숫자는 {input_num} 은 음수 입니다")
else :
    print(f"입력한 숫자는 {input_num} 은 0 입니다")

print("종료")