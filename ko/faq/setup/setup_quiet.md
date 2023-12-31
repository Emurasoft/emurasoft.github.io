# 질문. 대화 상자를 디스플레이 하지 않고 엠에디터를 어떻게 설치할 수 있나요?

일반 설치를 할 때, 대화 상자가 나타나게 되며, 사용자는 반드시 "다음" 버튼이나 설정 옵션을 클릭하셔야만 합니다.
그러나, 엠에디터를 회사 혹은 그룹내의 여러대의 컴퓨터에 설치할 때 설치를 자동화하기 위해 일괄처리 하시거나 파일을
스크립팅 하는 방법을 사용하실 수 있습니다. 버전 6 혹은 그 이후 버전에서는 설치를 위한 윈도우 설치자를 이용하실 수 있으며
"자동 모드" 설치가 가능합니다.

예를 들어, 엠에디터 설치 파일이 emed32\_13.0.0.exe이고, 다음 명령을 실행시킨 다면:

emed32\_13.0.0 /exenoui /q

이 초기 설정으로 어떤 대화상자 표시 없이도 엠에디터를 설치하실 수 있습니다. 만일 초기 설정을 바꾸고자 하신다면, 다음 옵션들을 이용하실 수 있습니다:

|     |     |
| --- | --- |
| NOCHECKUPDATES | 인터넷을 통해 정기적으로 EmEditor의 새로운 버전 확인을 비활성화합니다. |
| NOCONTEXTMENU | 익스플로러의 상황에 맞는 메뉴에 바로가기 추가를 비활성화합니다. |
| NODESKTOP | 바탕화면에 바로가기 추가를 비활성화합니다. |
| NOIEEDITOR | 인터넷 탐색기 HTML 편집기 목록에 EmEditor 추가를 비활성화합니다. |
| NOIEVIEW | 인터넷 탐색기에서 EmEditor로 소스 보기를 비활성화합니다. |
| NOPATH | PATH 환경 변수에 EmEditor의 경로 추가를 비활성화합니다. |
| NOSHORTCUT | 프로그램 메뉴에 바로가기 추가를 비활성화합니다. |
| NOTRAYICON | 트레이 아이콘을 비활성화합니다. |
| NOTXT | 텍스트 파일의 연결을 비활성화합니다. |
| REGNAME=name | 라이센스의 이름을 입력합니다. |
| REGKEY=xxxxxx | 등록 키를 입력합니다. |

예를 들어, 만일 등록키를 지정하고 라이센스의 이름을 지정해서 엠에디터를 설치하고자 한다면, 다음을 실행시키십시오:

emed32\_13.0.0 /exenoui /q REGKEY=xxxxx REGNAME=name

emed32\_13.0.0 /exenoui /q NODESKTOP=1

윈도우 설치자를 위한 많은 옵션들이 있습니다. 자세한 내용을 위해서 다음을 실행시키십시오:

emed64\_13.0.0.exe /?

그리고

msiexec /?

사용 가능한 명령의 목록을 디스플레이 하기 위해서 사용할 수 있습니다.

## 참고:

Windows Vista 이상에서, 사용자 계정 컨트롤 프롬프트를 피하려면 관리자 권한에서 설치관리자를 실행해야만 합니다. 예를 들어,
명령 프롬프트에서 설치 관리자를 실행하는 경우, SHIFT 키를 누른 상태에서 명령 프롬프트 아이콘을 마우스 오른쪽으로 클릭한 후 **관리자 권한** 으로 실행을 선택하여 명령 프롬프트 창을 열어야 합니다.
