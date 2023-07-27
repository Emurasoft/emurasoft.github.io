# 논리적 홈 또는 텍스트 시작점 선택 명령

## 요약

현재 논리 줄의 시작 또는 텍스트의 시작 부분으로 선택을 확장합니다.

## 설명

현재 논리 줄의 시작 부분으로 선택을 확장합니다. 문자 전에 공백이 존재한다면 현재 행의 첫 비공백 문자까지 선택을 확장합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>선택 확장 \>논리적 홈 또는 텍스트 시작점 선택
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_SHIFT_LOGICAL_HOME_TEXT (4334)```

## 매크로

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineLogical \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineLogical \| eeLineHomeText
```
