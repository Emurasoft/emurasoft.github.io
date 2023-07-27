# 세로 선택 명령

## 요약

세로 선택 모드로 전환합니다.

## 설명

세로 선택 모드로 전환합니다.
이 명령은 키보드로 여러 문자를 강조 표시 할수 있습니다.
화살표 키로 커서를 움직이면 선택이 확장되거나 축소됩니다.
[복사 명령](edit_copy) 또는 [자르기 명령](edit_cut) 을 선택하면
문자 선택 모드가 종료됩니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>선택 확장 \>세로 선택
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+Shift+F8

## 플러그인 명령 ID

```
EEID_SELECT_BOX (4155)```

## 매크로

## \[JavaScript\]

```
editor.ExecuteCommandByID(4155);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4155
```
