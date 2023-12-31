# 유형으로 정렬 명령

## 요약

유형별로 탭을 정렬합니다.

## 설명

유형별로 탭을 정렬합니다.
[**자동 정렬** 명령](auto_sort) 이 체크되어 있는 경우,
이 명령은 파일이 열려있거나 이름으로 저장되어 있을 때마다 사용되어 자동으로 정렬됩니다.
[**자동 정렬** 명령](auto_sort) 이 체크되어 있지 않은 경우,
이 명령은 한번만 사용됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **보기** \> **탭 정렬 방식** \> **유형**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_SORT_TYPE (4399)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4399);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4399
```
