# step12_extends.py

# 클래스 상속에 대해서 알아 보자

# 가상의 전화기를 찍어낼 클래스
class Phone :
    def call(self) :
        print("전화를 걸어요!")

# 가상의 핸드폰을 찍어낼 클래스 , Phone 클래스를 extends 해서 정의한다
class HandPhone(Phone) :
    def mobile_call(self) :
        print("이동중에 전화를 걸어요!")

    def take_picture(self) :
        print("100 만 화소의 사진을 찍어요 !")

class SmartPhone(HandPhone) :
    def do_internet(self) :
        print("인터넷을 해요!")

    def take_picture(self) :
        print("1000만 화소의 사진을 찍어요")

if __name__ == "__main__" :
    p1 : Phone = Phone()
    p1.call()

    print("-------------------------")

    p2 : HandPhone = HandPhone()
    p2.call()
    p2.mobile_call()
    p2.take_picture()

    print("-----------------------------")

    p3 : SmartPhone = SmartPhone()
    p3.call()
    p3.do_internet()
    p3.take_picture() # 오버라이드