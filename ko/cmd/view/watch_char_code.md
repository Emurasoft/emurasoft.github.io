# 문자 코드 값 명령

## 요약

유니코드 문자 값을 표시합니다.

## 설명

이 명령은 커서 위치의 유니코드 문자 값을 나타내는 대화상자를 표시합니다.
xxxx가 숫자 결합을 나타내는 U+xxxx 형식은 16 진수 유니코드 값입니다.
파일의 인코딩이 유니코드가 아닌 경우, ANSI 코드 값이 두자리 16진수로 나타납니다.

## 실행하는 방법

- 기본 메뉴:보기 \>문자 코드 값
- [모든 명령](../tools/all_commands):보기 >
문자 코드 값
- 도구 모음:
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+I

## 플러그인 명령 ID

```
EEID_WATCH_CHAR_CODE (4213)```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4213);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4213
```
