# Z 부터 A까지 정렬 명령

## 요약

내림차순으로 현재 열의 텍스트를 정렬합니다.

## 설명

내림차순으로 현재 열의 텍스트를 정렬합니다.
텍스트가 알파벳 문자(A-Z와 a-z)를 포함하지 않은 경우, 이 명령은 숫자 값으로 정렬을 시도합니다.

## 실행하는 방법

- 기본 메뉴:편집 \>구분된 값/정렬 \>Z 부터 A까지 정렬
- [모든 명령](../tools/all_commands):편집 \>구분된 값/정렬 \>Z 부터 A까지 정렬
- 도구 모음: ![](../../images/sortingz-a.gif)
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_SORT_TEXT_D (4478)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4478);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4478
```
