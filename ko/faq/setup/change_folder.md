# 질문. 설치폴더를 어떻게 바꿀 수 있나요?

초기값에서, 설치 폴더는 이전 버전과 같은 폴더 이거나 초기 설치인 경우에는 \\Program Files\\EmEditor입니다.
설치 폴더를 바꾸기 위해서, 명령 확인을 열고, TARGETDIR 옵션으로 설치자를 실행시키십시오.

예를 들어, 엠에디터 설치 파일이 emed700epx.msi이고 엠에디터를 C:\\path에 설치하고 싶다면,
다음의 명령을 실행하십시오:

emed700epx.msi TARGETDIR="C:\\path\\"

백슬레시 '\\'는 폴더 이름의 맨 끝에 반드시 필요합니다.

버전 하나 이상의 엠에디터가 같은 컴퓨터 상에서 존재할 수 없습니다.
만일 이전 버전이 이미 설치되었다면, 이전 버전을 먼저 지우거나 이전 버전과 같은 폴더에 새로운 버전을 설치하십시오
