# 점프 명령

## 요약

지정된 줄로 점프합니다.

## 설명

이 명령은 [**점프** 대화 상자](../../dlg/jump/index) 를 표시합니다.
대화 상자에서 줄 번호를 지정하고 문서는 지정된 줄로 점프합니다.

## 실행하는 방법

- 기본 메뉴: **편집** \> **점프**
- [모든 명령](../tools/all_commands): **편집** \> **고급**
\> **점프**
- 도구 모음: ![](../../images/jump.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+G

## 플러그인 명령 ID

```
EEID_JUMP (4139)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4139);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4139
```
