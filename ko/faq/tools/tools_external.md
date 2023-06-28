# 질문. 외부 도구 구성에는 예를 들어 무엇이 있습니까?

- **인터넷 익스플로러** 를 여십시오.

**명령**: C:\\Program Files\\Internet Explorer\\iexplore.exe

**인수**: $(Path)

**초기 디렉터리**: $(Dir)

**아이콘 경로**: C:\\Program Files\\Internet Explorer\\iexplore.exe

**파일 저장** 체크하십시오.

- **검색창** 을 여십시오.

**명령**: %WinDir%\\explorer.exe

**인수**: $(Dir)

**초기 디렉터리**: $(Dir)

**아이콘 경로**: %WinDir%\\explorer.exe

- **명령 확인** 열기

**명령**: %WinDir%\\system32\\cmd.exe

**인수**: $(Dir)

**초기 디렉터리**: $(Dir)

**아이콘 경로**: %WinDir%\\system32\\cmd.exe

- **Visual C++** 로 컴파일 하기.

**명령**: %WinDir%\\system32\\cmd.exe

**인수**: /k "C:\\Program Files\\Visual Studio\\Vc7\\bin\\vcvars32.bat"&&cl $(Path)

**초기 디렉터리**: $(Dir)

**아이콘 경로**: C:\\Program Files\\Visual Studio\\Common7\\IDE\\devenv.exe

**파일 저장** 체크해 주십시오.

- Run associated program

**명령**: $(Path)

**인수**:

**초기 디렉터리**: $(Dir)

**아이콘 경로**:

**파일 저장** 체크해 주십시오.

- 커서위치의 단어 혹은 선택된 단어의 **구글** 검색하기.

**명령**: http://google.com/search?q=$(CurText)

**인수**:

**초기 디렉터리**:

**아이콘 경로**:

- **Microsoft Visual SourceSafe** 에서 확인해 주십시오.

**명령**: %WinDir%\\system32\\cmd.exe

**인수**: /k C:\\(SourceSafe 경로)\\Common\\VSS\\win32\\SS.EXE checkout $/(Path)/$(파일name).$(Ext) -y(user name)

**초기 디렉터리**: $(Dir)

**아이콘 경로**: C:\\(SourceSafe 경로)\\Common\\VSS\\win32\\SSEXP.EXE

- Check in to **Microsoft Visual SourceSafe**

**명령**: %WinDir%\\system32\\cmd.exe

**인수**: /k C:\\(SourceSafe 경로)\\Common\\VSS\\win32\\SS.EXE checkin $/(Path)/$(파일name).$(Ext) -y(user name)

**초기 디렉터리**: $(Dir)

**아이콘 경로**: C:\\(SourceSafe 경로)\\Common\\VSS\\win32\\SSEXP.EXE

**파일 저장** 체크해 주십시오.

$(Path) 파일의 전체 경로 이름.

$(Dir) 파일의 디렉터리 이름.

$(파일name) 확장 없이 파일 이름.

$(Ext) 파일 이름 확장.

$(CurLine) 커서의 논리 줄 번호.

$(CurText) 선택되었을 시 선택된 텍스트 혹은 선택되지 않았을 시 커서에 단어.

또한 %WinDir%와 같은 환경 변수를 지정할 수 있습니다.