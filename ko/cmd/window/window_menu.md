# 문서 목록 명령

## 요약

지정된 문서로 전환합니다 (여러 문서).

## 설명

지정된 엠에디터 문서로 전환합니다. 지정된 문서가 최소화된 경우, 일반 크기로 복원합니다.
이 명령은 여러 메뉴 항목을 포함하고 있습니다.

## 실행하는 방법

- 기본 메뉴:창 \> (문서 이름)
- [모든 명령](../tools/all_commands):창 \> (문서 이름)
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
From EEID_WINDOW_MENU through EEID_WINDOW_MENU + 255 (from 5376 through 5376 + 255)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(5376 + i);  // i is an integer from 0
through 255
```

### \[VBScript\]

```
editor.ExecuteCommandByID 5376 + i   ' i is an integer from 0
through 255
```
