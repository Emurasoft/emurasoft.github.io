# 합자 명령

## 요약

합자를 삽입합니다.

## 설명

이 명령을 선택한 후에 a, o, A 또는 O를 입력하면 커서 위치에 합자 (æ, œ, Æ 또는 Œ)를 삽입하고
s를 입력하면 (ß)를 삽입합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>삽입
\>강조 표시/ 특수 문자 삽입 \>합자
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+7

## 플러그인 명령 ID

```
EEID_INSERT_LIGATURE (4309)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4309);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4309
```
