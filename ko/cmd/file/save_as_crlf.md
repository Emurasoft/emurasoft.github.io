# CR+LF로 저장 명령

## 요약

CR+LF로 저장합니다.

## 설명

이 명령은 모든 새로운 라인을 CR+LF로 변환 한 후 저장합니다 (Windows). 문서의 제목이 정해져 있지 않다면 저장하기 원하는 파일 이름을 입력할 수 있는 **다른 이름으로 저장** 대화 상자가 나타나게 됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **저장**
\> **다른 반환 코드로 저장** \> **CR+LF로 저장**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_SAVE_AS_CRLF (4105)```

## 매크로

## \[JavaScript\]

```
editor.ExecuteCommandByID(4105);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4105
```
