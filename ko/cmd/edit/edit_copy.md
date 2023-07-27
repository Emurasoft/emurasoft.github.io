# 복사 명령

## 요약

선택 영역이나 현재 줄을 복사하여 클립보드에 붙여 넣습니다.

## 설명

선택된 텍스트를 복사하여 클립보드로 이동합니다. 이 명령 후에 다른 위치로 커서를 움직여 [붙여넣기 명령](edit_paste) 을 실행 하여 선택 사항을 붙여 넣을 수 있습니다.

## 실행하는 방법

- 기본 메뉴:편집 \>복사
- [모든 명령](../tools/all_commands):편집 \>복사
\>복사
- 도구 모음: ![](../../images/copy.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+C 또는 CTRL+INSERT

## 플러그인 명령 ID

```
EEID_EDIT_COPY (4127)```

## 매크로

### \[JavaScript\]

```
document.selection.Copy(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.Copy eeCopyUnicode
```
