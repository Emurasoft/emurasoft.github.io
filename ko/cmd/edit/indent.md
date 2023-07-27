# 줄 들여쓰기 명령

## 요약

선택 영역에서 줄을 들여씁니다.

## 설명

선택된 영역 각 행의 시작점에 탭 문자를 삽입합니다. 여러 행이 동시에 선택된 경우, 이 명령은 [탭 삽입/줄 들여쓰기 명령](tab) 과
동일하게 작용됩니다.

## 실행하는 방법

- 기본 메뉴:편집 \>선택 변환 \>줄 들여쓰기
- [모든 명령](../tools/all_commands):편집 \>선택 변환 \>줄 들여쓰기
- 도구 모음: ![](../../images/indent.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_INDENT (4358)```

## 매크로

### \[JavaScript\]

```
document.selection.Indent();
```

### \[VBScript\]

```
document.selection.Indent
```
