# 논리 홈 또는 텍스트 시작점 명령

## 요약

현재 논리 줄 또는 텍스트의 시작점으로 커서를 이동합니다.

## 설명

현재 논리 줄 또는 텍스트의 시작점으로 커서를 이동합니다.
커서가 줄의 시작점의 공백 문자내에 있다면 이 명령은 커서를 그 줄의 공백이 아닌 첫 문자로 이동하게 합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **가로로 커서 이동** \> **논리 홈 또는 텍스트 시작점**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_LOGICAL_HOME_TEXT (4333)```

## 매크로

## \[JavaScript\]

```
document.selection.StartOfLine(false,eeLineLogical \| eeLineHomeText);
```

## \[VBScript\]

```
document.selection.StartOfLine false,eeLineLogical 또는 eeLineHomeText
```
