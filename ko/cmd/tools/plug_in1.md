# 플러그 인 목록 명령

## 요약

지정된 플러그 인을 실행합니다 (여러 항목).

## 설명

이 명령은 여러 메뉴 항목을 포함하고 있습니다.
이 명령은 지정된 플러그 인을 실행합니다.
사용 가능한 플러그 인은 [**플러그인 사용자 지정** 대화 상자](../../dlg/plugins/index) 에
정의되어 있습니다.

## 실행하는 방법

- 기본 메뉴: **도구** \> **플러그 인** \> (**플러그 인 이름**)
- [모든 명령](all_commands): **플러그 인**
\> (**플러그 인 이름**)
- 도구 모음: 플러그 인 도구 모음의 각 버튼
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
From EEID_PLUG_IN1 through EEID_PLUG_IN1 + 255 (from 5632 through 5632 +
```
255)

## 매크로

## \[JavaScript\]

```
editor.ExecuteCommandByID(5632+i);  // i is an integer from 0 through
255
```

## \[VBScript\]

```
editor.ExecuteCommandByID 5632+i  ' i is an integer from 0 through 255
```
