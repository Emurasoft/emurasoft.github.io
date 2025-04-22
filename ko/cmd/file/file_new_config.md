# 새 구성 리스트 명령

## 요약

지정된 구성으로 새 파일을 생성합니다 (여러 항목).

## 설명

이 명령은 여러 메뉴 항목으로 구성되어 있습니다. 미리 정의된 구성을 선택할 수 있습니다. 이 명령은 새로운 파일을 지정된 구성으로 생성합니다. [**구성 정의** 대화 상자](../../dlg/configurations/index) 안에서 구성을 편집, 삭제 및 추가 할 수 있습니다.

## 실행하는 방법

- 기본 메뉴: **파일** \> **새로 만들기 \> (구성 이름)**
- [모든 명령](../tools/all_commands): **파일** \> **새로 만들기 \> (구성 이름)**
- 도구 모음: ![](../../images/filenew.png) (화살표)
\+ (구성 이름)
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_FILE_NEW_CONFIG 부터 ID_FILE_NEW_CONFIG 까지 + 255 (7168 부터
```
7168 까지 + 255)

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(7168 + i);  // i is an integer from 0
through 255
```

### \[VBScript\]

```
editor.ExecuteCommandByID 7168 + i  ' i is an integer from 0 through 255
```
