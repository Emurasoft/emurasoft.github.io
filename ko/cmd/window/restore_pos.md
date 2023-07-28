# 창 위치 복원 명령

## 요약

이전에 저장했던 위치로 창을 복원시킵니다.

## 설명

이 명령은 이전에 저장했던 위치로 창을 복원시킵니다.
이 명령을 사용하기 위해서는, 먼저
[**사용자 지정 대화 상자**](../../dlg/customize/index) [**창 탭**](../../dlg/customize/window/index) 의
**현재 창 위치 저장** 버튼을 눌러 창의 위치를 저장하여야 합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **창** \> **복원** \> **창 위치 복원**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL + 9

## 플러그인 명령 ID

```
EEID_RESTORE_POS (4406)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4406);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4406
```
