# 줄 복사 명령

## 요약

현재 줄을 복사하여 클립보드에 붙여 넣습니다.

## 설명

커서에 위치한 논리 줄을 복사하여 클립보드에 넣습니다.
이 명령 후에 다른 위치로 커서를 움직여 [붙여넣기 명령](edit_paste) 을 실행 하여 선택 사항을 붙여 넣을 수 있습니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>복사
\>줄 복사
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_EDIT_COPY_LINE (4192)```

## 매크로

### \[JavaScript\]

```
document.selection.SelectLine();
document.selection.Copy(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.SelectLine
document.selection.Copy eeCopyUnicode
```
