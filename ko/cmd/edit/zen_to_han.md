# 반자 명령

## 요약

전각 문자를 반각 문자로 변환합니다.

## 설명

전각 문자를 반각 문자로 변환합니다. 전각 문자는 일반적으로 동부 아시아 글꼴에 포함되어 있습니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **선택 변환** \> **반자**
- [모든 명령](../tools/all_commands): **편집** \> **선택 변환** \> **반자**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_ZEN_TO_HAN (4151)```

## 매크로

### \[JavaScript\]

```
document.selection.ChangeWidth(eeWidthHalfWidth \| eeWidthAllTypes);
```

### \[VBScript\]

```
document.selection.ChangeWidth eeWidthHalfWidth 또는 eeWidthAllTypes
```
