# 사전 명령

### 요약

> 맞춤법을 확인하기 위해 이 사전을 선택합니다 (여러 항목).

### 설명

> 맞춤법을 확인하기 위해 이 사전을 선택합니다. 엠에디터의 설치 프로그램은 미국 영어 사전을 포함하고 있습니다.
> 추가 사전은 **[OpenOffice.org wiki](http://wiki.services.openoffice.org/wiki/Dictionaries)**
> 에서 다운로드 할수 있습니다.
> 사전을 추가하기 위해서는, **\*.dic** 과 **\*.aff** 파일을 복사하여 엠에디터 설치 폴더의 **사전** 하위 폴더에
> 넣습니다. (일반적으로, C:\\Program Files\\EmEditor\\Dictionaries 입니다.)

### 실행하는 방법

- 기본 메뉴: **편집** \> **맞춤법** \> **사전** \> **(사전)**
- [모든 명령](../tools/all_commands): **편집** \> **맞춤법** \> **사전** \> **(사전)**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

### 플러그인 명령 ID

- From EEID\_SELECT\_DICTIONARY through EEID\_SELECT\_DICTIONARY + 255 (from 22016 through 22016 + 255)

### 매크로

#### \[JavaScript\]

> editor.ExecuteCommandByID(22016 + i);  // i is an integer from 0 through 255

#### \[VBScript\]

> editor.ExecuteCommandByID 22016 + i  ' i is an integer from 0 through 255