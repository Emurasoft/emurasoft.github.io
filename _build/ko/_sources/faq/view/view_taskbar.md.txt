# 질문. 작업 표시줄의 트레이 아이콘을 즐겨찾기 아이콘으로 바꿀 수 있습니까?

네, 레지스트리 편집기(RegEdit.exe)를 실행시키고 난 후에 HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorv3\\Common을 찾아주십시오. 값이 REG\_SZ인 TrayIcon파일을 생성시키고 아이콘 파일 경로를 설정하신 후 값이 REG\_DWORD인 TrayIcon파일를 생성시키고 아이콘 색인을 설정해 주십시오.