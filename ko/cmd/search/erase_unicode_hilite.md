# 유니코드 강조 표시 삭제 명령

## 요약

저장할 인코딩으로 변환 할 수 없는 유니코드 문자의 강조 표시를 삭제합니다.

## 설명

저장할 인코딩으로 변환 할 수 없는 검색된 유니코드 문자의 강조 표시를 초기화합니다.
이 명령은 [**다음 유니코드 찾기** \
명령](find_next_unicode) 또는 [**이전 유니코드 찾기** \
명령](find_prev_unicode) 을 통해 설정된 저장 인코딩 또한 초기화 합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **검색** \> **유니코드 강조 표시 삭제**
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: ALT+F9

## 플러그인 명령 ID

```
EEID_ERASE_UNICODE_HILITE (4377)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4377);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4377
```
