# 새 행 삽입 명령

## 요약

현재 선택 배치 지점에 새로운 행을 삽입합니다.

## 설명

현재 선택 배치 지점에 새로운 행을 삽입합니다. [**줄 나누기** 명령](split_lines) 과 비슷하지만
이 명령은 새로운 행 이전에 각 행의 공백을 제거하지 않습니다. 새 행 방법은 현재 행에서 사용되는 방법과 일치합니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **선택 변환** \> **새 행 삽입**
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** > **새 행 삽입**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_INSERT_CR_WRAP (4143)```

## 매크로

### \[JavaScript\]

```
document.selection.Format(eeFormatInsertNL);
```

### \[VBScript\]

```
document.selection.Format eeFormatInsertNL
```
