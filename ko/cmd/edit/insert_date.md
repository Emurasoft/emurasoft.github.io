# 시간 및 날짜 명령

## 요약

시간 및 날짜를 삽입합니다.

## 설명

커서 위치에 현재 시간 및 날짜를 삽입합니다. 이 명령은 시간, 공백, 날짜 순으로 삽입합니다.
시간과 날짜에 사용되는 형식은 Windows에서제어판 의국가 및 언어 옵션 을 선택 한 후날짜 및 시간 을 선택하여
구성 할 수 있습니다.

## 실행하는 방법

- 기본 메뉴:편집 \>고급 \>시간 및 날짜
- [모든 명령](../tools/all_commands):편집 \>삽입
\>시간 및 날짜
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: 없음

## 플러그인 명령 ID

```
EEID_INSERT_DATE (4137)```

## 매크로

### \[JavaScript\]

```
document.selection.InsertDate(eeDateTimeDate);
```

### \[VBScript\]

```
document.selection.InsertDate eeDateTimeDate
```
