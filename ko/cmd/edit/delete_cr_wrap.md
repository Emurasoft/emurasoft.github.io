# 새 행 제거 명령

## 요약

현재 선택 배치 지점에 새로운 행을 제거합니다.

## 설명

현재 선택 배치 지점에 새로운 행을 제거합니다.
[**줄 합치기** 명령](join_lines) 과 비슷하지만 줄 바꾸는 포인트에 있는 각 행에 공백을 삽입하지 않습니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **선택 변환** \> **새 행 제거**
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** \> **새 행 제거**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_DELETE_CR_WRAP (4144)```

## 매크로

### \[JavaScript\]

```
document.selection.Format(eeFormatDeleteNL);
```

### \[VBScript\]

```
document.selection.Format eeFormatDeleteNL
```
