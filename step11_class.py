#step11_class.py


# 간단한 Car 클래스 정의
class Car :

    def drive(self) :
        print("달려요 !")

print(__name__)

# 현재 파일이 main 으로 실행되었을 때만 실행할 코드는 아래의 코드 블럭에 넣어야 한다.
# main 으로 실행되었다는 의미는 이 file 에서 run 버튼을 눌렀다는 의미이다.
# 사실 실제 python 으로 app 만들고 실행하려면 단일 진입점이 있어야 한다.
if __name__ == "__main__" :
    # Car 클래스를 이용해서 객체를 생성하고 그 참조값을 c1 이라는 이름의 Car type 변수에 담기
    c1 : Car = Car()
    # c1에 . 을 찍으면 해당 객체를 사용할 수 있다.
    c1.drive()