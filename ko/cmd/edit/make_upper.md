# 대문자로 명령

## 요약

선택 영역을 모두 대문자로 변환합니다.

## 설명

선택 영역을 모두 대문자로 변환합니다. 예를 들어, a 는 A가 되며 ä 는 Ä로, λ 는Λ가 됩니다.

## 실행하는 방법

- 기본 메뉴: **편집** > **선택 변환** \> **대문자로**
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** \> **대문자로**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+U

## 플러그인 명령 ID

```
EEID_MAKE_UPPER (4149)```

## 매크로

### \[JavaScript\]

```
document.selection.ChangeCase(eeCaseUpperCase);
```

### \[VBScript\]

```
document.selection.ChangeCase eeCaseUpperCase
```
