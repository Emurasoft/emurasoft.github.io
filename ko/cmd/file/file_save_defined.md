# 인코딩하여 저장하기 리스트 명령

## 요약

지정된 인코딩을 사용하여 현재 파일을 저장합니다 (여러 항목).

## 설명

이 명령은 사전에 정의된 인코딩을 선택할 수 있는 여러 메뉴 항목으로 구성되어 있습니다.
문서의 이름이 지정되어 있다면 이 명령은 지정된 인코딩을 사용하여 현재 파일을 저장합니다.
문서의 제목이 정해져 있지 않다면 저장하기 원하는 파일 이름을 입력할 수 있는 **다른 이름으로 저장** 대화 상자가 나타나게 됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **저장**
\> **인코딩으로 저장** \> **(인코딩 선택)**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## Plug-ins command ID

- From EEID\_FILE\_SAVE\_DEFINED through ID\_FILE\_SAVE\_DEFINED + 255 (from 7680
through 7680 + 255)

## 매크로

## \[JavaScript\]

```
editor.ExecuteCommandByID(7680 + i);  // i is an integer from 0
through 255
```

## \[VBScript\]

```
editor.ExecuteCommandByID 7680  + i  ' i is an integer from 0
through 255
```
