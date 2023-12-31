# 바꿀 단어 설정 명령

## 요약

현재 단어를 바꿀 문자열로 설정합니다.

## 설명

커서 위치의 단어를 [**다음 바꾸기** 명령](replace_next) 을 위한 대체열로 설정합니다.
이 명령을 실행 한 후에 [**다음 바꾸기** 명령](replace_next) 을 선택하면, 이 명령을 통해 지정된 단어와
다음 쿼리 단어를 즉시 대체합니다.
[**바꾸기** 대화 상자](../../dlg/replace/index) 에 **\> 버튼** 을 클릭하였을 때 보이는 메뉴에
사용자 지정이 선택되어 있는 경우, 이 명령을 통해 지정된 단어를 기본값으로 나타냅니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **검색** \> **바꿀 단어 설정**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_RETRIEVE_REPLACE_TEXT (4446)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4446);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4446
```
