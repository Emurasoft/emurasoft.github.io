# 작업 영역 저장, 저장 후 모두 닫기 명령

## 요약

작업 영역을 저장하고 열려있는 모든 파일을 저장 후 닫습니다.

## 설명

이 명령은 작업 영역과 열려있는 모든 문서를 저장하고 모든 문서를 닫습니다.
이 명령은 [**작업 영역 저장** 명령](save_workspace) 후에 [**저장 후 모두 닫기** 명령](save_exit_all) 을 실행한 것과 동일하게 적용됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **닫기**
\> **작업 영역 저장, 저장 후 모두 닫기**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_SAVE_WORKSPACE_EXIT_ALL (4331)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4331);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4331
```
