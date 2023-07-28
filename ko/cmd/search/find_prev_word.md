# 이전 단어 찾기 명령

## 요약

현재 단어의 이전 항목을 찾습니다.

## 설명

문자열이 선택되어 있는 경우, 지정된 문자열의 이전 항목을 찾습니다. 그렇지 않은 경우에는, 커서 위치에 해당하는 단어의
이전 항목을 찾습니다.

## 실행하는 방법

- 기본 메뉴: **검색** \> **이전 단어 찾기**
- [모든 명령](../tools/all_commands): **검색** \> **이전 단어 찾기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+F3

## 플러그인 명령 ID

```
EEID_FIND_PREV_WORD (4205)```

## 매크로

### \[JavaScript\]

```
document.selection.FindRepeat(eeFindRepeatPrevious \| eeFindRepeatWord);
```

### \[VBScript\]

```
document.selection.FindRepeat eeFindRepeatPrevious 또는 eeFindRepeatWord
```
