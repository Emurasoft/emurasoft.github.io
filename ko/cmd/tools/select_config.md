# 구성 목록 명령

## 요약

지정된 구성을 선택합니다 (여러 항목).

## 설명

이 명령은 여러 메뉴 항목을 포함하고 있습니다.
이 명령은 현재 구성으로 지정된 구성을 선택합니다.
현재 구성은 상태 표시줄에 표시됩니다.
엠에디터는 새로운 문서를 생성할 때 기본적으로 **Text** 구성을 사용합니다.

## 실행하는 방법

- 기본 메뉴: **도구** \> **구성 선택** \> (**구성 이름**)
- [모든 명령](all_commands): **도구** >
**구성 선택** \> (**구성 이름**)
- 도구 모음: ![](../../images/configpopup.gif) (화살표 위)\>
(**구성 이름**)
- 상태 표시줄: (구성 이름을 두 번 클릭) \> (**구성 이름**)
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
From EEID_SELECT_CONFIG through EEID_SELECT_CONFIG + 255 (from 5120
```
through 5120 + 255)

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(5120 + i);  // i is an integer from 0
through 255
```

### or

document.ConfigName = "(configuration name)";

### \[VBScript\]

```
editor.ExecuteCommandByID 5120 + i   ' i is an integer from 0
through 255
```

### or

document.ConfigName = "(configuration name)"
