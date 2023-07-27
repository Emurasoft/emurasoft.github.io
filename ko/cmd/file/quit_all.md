# 저장 없이 모두 닫기 명령

## 요약

열려있는 모든 파일을 저장하지 않고 닫습니다.

## 설명

이 명령은 열려있는 모든 파일을 저장하지 않고 닫습니다. 모든 변경 사항은 취소됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):파일 \>닫기
\>저장 없이 모두 닫기
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_QUIT_ALL (4363)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4363);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4363
```
