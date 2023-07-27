# 단어 선택 명령

## 요약

현재 커서 위치의 오른쪽 단어를 선택합니다.

## 설명

현재 커서 위치의 오른쪽 단어를 선택합니다.
이 명령은 두 공백 문자 사이의 모든 텍스트 문자를 선택합니다. 공백은 커서가 공백이전에 위치했을 경우에만 선택됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>선택 확장 \>단어 선택
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: ALT+F8

## 플러그인 명령 ID

```
EEID_SELECT_WORD (4251)```

## 매크로

### \[JavaScript\]

```
document.selection.SelectWord();
```

### \[VBScript\]

```
document.selection.SelectWord
```
