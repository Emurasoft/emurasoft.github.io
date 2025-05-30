# 단어 완성 플러그인을 이용하기

**단어 완성** 플러그인은 엠에디터 Professioanl으로 초기화되어 설치되어 있습니다. 문서에 입력하는대로
이 플러그인은 이전에 사용된 단어로 채워지는것이 보일것이며, 엠에디터에 정의된 단어에 강조표시되어질 것입니다.

사용자의 입력을 완성하기 위해서 목록이 보여지고 이 중에서 고를 수 있게 됩니다.

단어 완성 플러그인은 최근 검색된 문자열을 완성시킬수도 있습니다. 이 과정은 단어 완성과 같으나,
단어를 완정하는 대신에, 플러그인으로 문자열을 완성시킬 수 있습니다.

단어 완성 플러그인을 사용하는 방법:

1. **플러그인** 바에서 ![](../../images/wordcomplete.png) 를 클릭해 주십시오.
혹은, 도구 메뉴에서, **플러그인** 을 가리킨 후에, **단어 완성** 을 클릭하면 이것에 체크표시 되어집니다.
2. 문서에 삽입하고 싶은 단어의 처음 몇 글자를 입력하시고,
이전에 사용된 단어와 엠에디터에서 정의된 강조표시 된 단어로 채워진 목록이 나타날 것입니다.
3. **위로** 혹은 **아래로** 키를 이용해서 삽입할 단어를 선택하고 **엔터** 를 눌러 주십시오.

## 플러그인 속성

### 사전

|     |     |
| --- | --- |
| **강조표시 단어** | 구성 속성의 **강조표시 (1) 탭** 에서 정의된 문자열<br> 이 후보로써 사용되어집니다. |
| **문서에서 사용된 단어** | 현재 문서의 단어는 후보로써 사용됩니다. |
| **문자열 제한** | 현재 커서 위치의 이전과 이후에 지정된 줄에서의 문자 제한합니다. |
| **이전 문서를 포함** | 후보 목록을 위해 이전 문서를 포함합니다. |
| **그룹에 모든 문서 포함** | 같은 그룹 윈도우에 모든 문서를 포함합니다. |
| **같은 구성인 경우에만** | 현재 문서와 같은 구성인 경우에만 모든 문서를 포함합니다. |
| **사전 파일의 단어** | 구분된 파일의 단어는 후보로 사용됩니다. |
| **사전 파일** | 전체 경로 그리고 분리 파일의 이름은 지원 목록으로써 사용되어야 합니다. |
| **무료 형식(만약 체크되지 않았다면, 줄마다)** | 스페이스로 구분된 어떤 파일이든 사전 파일로써 이용될 수 있습니다. 만일 체크되지 않았다면, 각 줄은 반드시 새로운 줄로 나뉘어 져야 됩니다. |
| **클립보드 내용** | 클립보드의 단어는 후보로써 사용될 수 있습니다. |
| **파일 이름** | 같은 파일에 있는 파일 이름은 후보로써 사용될 수 있습니다. |
| **문자열 찾기** | 이전에 찾은 문자열의 기록을 보여줍니다. |
| **비율 새로고침** | 후보자가 얼마나 자주 새로고침 되는지를 지정합니다, 후보자 목록은 최근에 입력된 단어로 업데이트 됩니다.<br> 이 비율이 더 높을수록, 목록이 업데이트 되기 전에 입력되어야 합니다. |

### 일치 조건

|     |     |
| --- | --- |
| **대/소문자 일치** | 대/소문자가 일치되는지 지정하십시오. 예를 들어, **ABC** 와 **abc** 가 현재 문서에서 찾을 수 있다고 해 봅시다.(혹은 사전 파일) 만일 **절대** 가 선택되어 있으면, **ABC** 혹은 **abc** 가 후보로써 사용될 수 있으며,<br> 그리고 **A** 혹은 **a** 를 입력하게 되면, **ABC** 혹은 **abc** 가 디스플레이 됩니다. 만일 **후보자 안에서** 가 선택되어 있으면, **ABC** 와 **abc** 둘 다 후보자로 사용되며, **A** 혹은 **a** 를 입력하게 되면 **ABC** 와 **abc** 가 디스플레이 됩니다. 만일 **후보자와 입력 모두** 가 선택되여졌다면, **ABC** 와 **abc** 가 후보자로 사용되지만, **A** 는 **ABC** 로 그리고 **a** 를 입력하면 **abc** 로 디스플레이 됩니다. |
| **우선순위** | 만일 **최근 사용된 단어가 처음으로** 가 선택되어 졌다면, 가장 마지막에 선택된 단어가 초기에 후보자 목록이 디스플레이 될 때 선택되어집니다. 만일 **사전순** 이 선택되어 있으면, 일치된 항목중 가장 상위 항목이 초기 선택으로 선택되어집니다. |
| **단어 입력** | 만일 **일반 단어** 가 선택되어 지면, 각 단어는 문자로 시작되며 문자 혹은 숙자로 끝나게 됩니다. 만일 **점 구문** 이 선택되게 되면, 각 단어는 점(**.**)을 포함하게 됩니다. 만일 **HTML/XML** 가 선택되어 지면, 각 단어는 **<** 혹은 **&** 로 시작되며, 이것은 단어의 중간에서 **/** 혹은 **-** 을 포함할 수 있으며, **>** 혹은 **;** 으로 끝날 수 있습니다.<br> **사용자 지정** 이 선택되었으면, 사용자는 어떻게 단어가 텍스트 상자에 배열될 것인지 정의할 수 있습니다. |
| **첫번째 문자** | 만일 **사용자 지정** 이 **단어 유형** 드롭다운 목록에서 선택되어 있으면, 각 단어가 시작할 수 있는 첫번째 문자를 입력하십시오. |
| **중간 문자** | 만일 **사용자 지정** 이 **단어 유형** 드롭다운 목록에서 선택되어 있으면, 첫번째 문자와 마지막 문자 사이에 들어갈 수 있는 각 단어를 문자와 숫자를 입력하십시오. |
| **마지막 문자** | 만일 **사용자 지정** 이 **단어 유형** 드롭다운 목록에 선택되어 있으면, 각 단어가 끝날 수 있는 마지막 단어를 입력해 주십시오. 이 때, 첫번째 혹은 중간 문자가 있어서는 안됩니다. |

### 옵션

|     |     |
| --- | --- |
| **후보자 목록에서 아이콘을 디스플레이** | 후보자 목록에서 각 항목의 왼쪽에 있는 작은 아이콘을 디스플레이합니다. |
| **하나의 후보자가 사용가능시, 자동 완성** | 사용자가 키보드 바로가기를 입력할 때, 하나의 항목이 후보를 위해 사용가능 할 때, 자동 완성 **후보 순서 보이기**(통상적으로 **CTRL** + **SPACE**)을 위한 플러그인을 허용합니다. |
| **후보 목록에서 강조표시 색을 사용하기** | 강조표시된 줄로 정의된 색으로 후보 목록에 강조표시합니다. |
| **후보 목록이 없을 때, 자동으로 목록을 숨기기** | 입력하는 단어와 일치하는 항목이 없을 때 후보 목록을 자동으로 숨깁니다. |
| **후보 목록에서 일치된 단어만 보이기** | 일치된 단어로만 후보 목록 제한하빈다. |
| **일치된 그리고 같은 길이 단어를 후보 목록에서 제외** | 입력된 단어와 같은 길이로 일치된 단어를 자동적으로 제외시킵니다. |
| **입력된 것처럼 후보 목록 자동으로 보이기** | 입력한대로 후보목록을 자동적으로 디스플레이합니다. |
| **문자의 개수** | 후보목록이 자동적으로 디스플레이 될 때 까지 플러그인이 기다리고 있는 문자의 개수 |
| **지연 시간** | 일치 단어를 찾고 난 후 부터 후보목록을 자동적으로 디스플레이 할 때까지 플러그인이 기다리고 있는 시간입니다. |

### 키보드

|     |     |
| --- | --- |
|  | 사용가능한 명령 목록화 합니다. |
| **새로운 바로가기 키 입력** | 선택된 명령을 위해서 바로가기 키를 입력합니다. |
| **현재 키** | 현재 키가 선택된 명령에 할당되었습니다. |
| **설명** | 선택된 명령을 위해 설명합니다. |

## 팁

초기값에서, 엠에디터는 사용자가 단어 입력을 시작할 때, 키 입력과 자동 목록 디스플레이를 디스플레이 합니다. 이 행동을 비활성화 하시려면, **플러그인** 모음의 플러그인 버튼을 오른쪽 클릭 한 후, **속성** 을 선택하시고 **입력된 후보 목록 자동으로 보이기** 체크 박스의 체크를 지우십시오.
여전히 키보드 바로가기를 입력해서 목록을 디스플레이 할 수 있습니다.
초기 키보드 바로가기는 **CTRL + SPACE** 이며, 다른 키보드 바로가기를 **속성** 에서 키보드 탭에서 선택함으로써 할당할 수 있습니다.
**플러그인 속성** 의 옵션은 각각의 구성의 설정이 될 수 있습니다.
