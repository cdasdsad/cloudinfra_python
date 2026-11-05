# step11_class3.py


class YourCar:

    def __init__(self):
        pass

    def drive():
        print("달려요!")


class OurCar:
    # 생성사제 str type 을 전달 받는 구조
    def __init__(self, name: str):
        # 전달받은 문자열을 객체 고유의 저장소(필드)에 저장한다
        self.name = name

    def drive(self):
        # 필드에 저장된 내용을 참조해서 동작하기
        print(f"{self.name}이(가) 달려요")


# main 으로 실행 되었을 때만 실행할 code 블럭 (app 의 단일 진입점이 된다.)
if __name__ == "__main__":
    YourCar()

    c1: OurCar = OurCar("소나타")
    c1.drive()

    c2: OurCar = OurCar("아반떼")
    c2.drive()

    print("main 함수가 종료 됩니다.")
