# 탭 해제 명령

## 요약

탭을 해당하는 공백으로 변환합니다.

## 설명

각 행의 시작점에 선택된 탭을 공백으로 변환합니다. 탭 설정 공백의 수는 [탭/들여쓰기 대화 상자](../../dlg/properties/general/indent/index) 에서 설정할 수 있습니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>선택 변환 \>탭 해제
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_UNTABIFY (4357)```

## 매크로

### \[JavaScript\]

```
document.selection.Untabify();
```

### \[VBScript\]

```
document.selection.Untabify
```
