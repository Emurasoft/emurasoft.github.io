# 문자에 맞춰 줄 바꿈 명령

## 요약

문자의 지정된 숫자에 따라 줄을 바꿉니다.

## 설명

문자의 지정된 숫자 (바이트)에 따라 줄을 바꿉니다.
이 명령은[구성 속성](../../dlg/properties/index) 대화 상자의
[일반 탭](../../dlg/properties/general/index) 에서
줄 바꿈 드롭다운 리스트 박스로 부터지정된 문자 를 선택한 것과 동일하게
작용됩니다.

## 실행하는 방법

- 기본 메뉴:보기 \>문자에 맞춰 줄 바꿈
- [모든 명령](../tools/all_commands):보기 >
문자에 맞춰 줄 바꿈
- 도구 모음: ![](../../images/wrapbychar.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+2

## 플러그인 명령 ID

```
EEID_WRAP_BY_CHAR (4209)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4209);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4209
```
