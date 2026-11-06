import os

# 1. 저장할 파일의 경로 설정 (현재 작업 폴더의 user_input.txt)
save_path = os.path.join(os.getcwd(), "user_input.txt")
    
# 2. input() 함수로 사용자에게 문자열 입력받기
user_text = input("파일에 저장할 내용을 입력하세요: ")
    
    # 3. 입력받은 내용을 파일에 쓰기 ("w" 모드이므로 매번 새로 덮어씁니다)
with open(save_path, "a", encoding="utf-8") as f:
    # 입력받은 문자열 끝에 줄바꿈(\n)을 추가해 줍니다.
    f.write(user_text + "\n")
        
print(f"성공적으로 '{save_path}'에 저장되었습니다.")