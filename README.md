# python 기초 수업내용 입니다.
- 하나
- 두울
- 세엣

# SSH 키 인증 (개인키/공개키)
작성일: 2026-11-02 | 환경: Windows + Git Bash, VMware 서버, MobaXterm

## 1. 한 줄 요약
비밀번호 대신 "열쇠 쌍"으로 서버에 로그인하는 방법.
공개키(자물쇠)는 서버에 두고, 개인키(열쇠)는 내 PC에만 둔다.

## 2. 왜 쓰나
- 비밀번호는 유출/무차별 대입에 약하다
- 클라우드(AWS 등) 서버는 기본이 키 인증이다
- GitHub 연결, 자동 배포에도 같은 방식을 쓴다

## 3. 개념 (그림으로)
내 PC [개인키] --서명--> 서버 [공개키로 검증] --> 로그인 허용
※ 개인키는 네트워크로 전송되지 않는다

| 구분 | 파일 | 둘 곳 | 공유 |
|---|---|---|---|
| 개인키 | vmware_key.pem | 내 PC | 절대 금지 |
| 공개키 | vmware_key.pem.pub | 서버 ~/.ssh/authorized_keys | 가능 |

## 4. 따라 하기 (순서대로)
### 4-1. 키 만들기 (내 PC, Git Bash)
​```bash
ssh-keygen -t ed25519 -f vmware_key.pem
# 실습용은 -N "" 로 암호 없이 생성 / 실무는 passphrase 권장
​```
→ 결과: 개인키와 .pub 공개키 2개 생성 (ls로 확인)

### 4-2. 공개키를 서버에 등록 (서버에서)
​```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
cat vmware_key.pem.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
​```
→ 왜 chmod? 권한이 느슨하면 SSH가 접속을 거부한다

### 4-3. 접속하기
- 터미널: `ssh -i vmware_key.pem <사용자>@<서버IP>`
- MobaXterm: Session → SSH → Use private key에 개인키 선택
(캡처 위치: 이 아래에 붙여넣기)

## 5. 막혔던 것 / 에러 모음
| 증상 | 원인 | 해결 |
|---|---|---|
| Permission denied (publickey) | 공개키 미등록 or 권한 문제 | 4-2 재확인, chmod 확인 |
| UNPROTECTED PRIVATE KEY FILE | 개인키 권한이 느슨함 | chmod 600 <개인키> |
| (여기에 직접 겪은 에러 추가) | | |

## 6. 응용 (나중에 해볼 것)
- [ ] ~/.ssh/config로 별칭 만들기 (`ssh vm`)
- [ ] GitHub SSH 연결
- [ ] 비밀번호 로그인 차단 + root 로그인 차단
- [ ] ssh-agent로 passphrase 한 번만 입력

## 7. 주의사항
- 개인키는 GitHub에 올리지 않기, 메신저로 보내지 않기
- 서버 보안 설정을 바꿀 때는 기존 접속 창을 닫지 않고 새 창으로 테스트하기

## 8. 관련 노트
- Git 원격 저장소 연결 (remote set-url)