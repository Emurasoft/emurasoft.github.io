# 왼쪽 문자로 명령

## 요약

커서를 한 문자 왼쪽으로 이동합니다.

## 설명

커서를 한 문자 왼쪽으로 이동합니다.
커서가 줄의 시작점에 위치하는 경우, 이 명령으로 이전 줄의 마지막 점으로 이동하게 됩니다.
왼쪽 화살표키를 누르는 것과 동일시 작용됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **가로로 커서 이동** \> **왼쪽 문자로**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: LEFT ARROW

## 플러그인 명령 ID

```
EEID_LEFT (4157)```

## 매크로

### \[JavaScript\]

```
document.selection.CharLeft(false,1);
```

### \[VBScript\]

```
document.selection.CharLeft false,1
```
