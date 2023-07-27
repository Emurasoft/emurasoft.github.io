# 줄 마지막에 공백 삭제 명령

## 요약

현제 문서의 모든 줄의 마지막에 있는 공백을 삭제합니다.

## 설명

현재 문서 전체에서 텍스트 문자와 케리지 반환 부호 사이의 공백을 삭제합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>삭제 \>줄 마지막에 공백 삭제
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_TRIM_RIGHT (4278)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4278);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4278
```
