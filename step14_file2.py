# step14_file2.py
import os

if __name__ == "__main__" :

    # 새로운 파일을 만들어서 문자열을 파일에 출력하기

    letter_path = os.path.join(os.getcwd(), "letter.txt")

    # "w" 는 없으면 새로 파일을 만들고 write, 있으면 기존 내용을 덮어쓰기
    with open(letter_path, "w", encoding="utf-8") as f :
        f.write("To my Friend \n")
        f.write("Hello \n")
        f.write("Bye \n")

    with open(letter_path, "r", encoding = "utf-8") as f2 :
           result2 = f2.read()
           print(result2) 