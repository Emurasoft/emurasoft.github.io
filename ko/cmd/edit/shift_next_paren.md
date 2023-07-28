# 일치 괄호/대괄호 선택 명령

## 요약

일치하는 괄호/대괄호까지 선택을 확장합니다.

## 설명

이 명령은 커서가 여는/닫히는 괄호나 대괄호에 위치하는 경우, 선택의 범위를 일치하는 닫히는/여는 괄호/대괄호까지 확장합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **편집** \> **선택 확장** \> **일치 괄호/대괄호 선택**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+\]

## 플러그인 명령 ID

```
EEID_SHIFT_NEXT_PAREN (4277)```

## 매크로

### \[JavaScript\]

```
document.selection.GoToBrace(true);
```

### \[VBScript\]

```
document.selection.GoToBrace true
```
