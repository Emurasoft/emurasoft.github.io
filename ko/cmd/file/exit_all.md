# 모두 닫기 명령

## 요약

열려있는 모든 파일을 닫고 엠에디터를 끝냅니다.

## 설명

이 명령은 열려있는 모든 파일을 닫습니다. 파일의 변경 사항이 있다면 그 변경 사항을 저장 할 것인지 묻는 확인 메시지가 나타납니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands): **파일** \> **닫기**
\> **모두 닫기**
- 도구 모음: ![](../../images/exitall.png)
- 상태 표시줄: 없음
- 기본 바로 가기 키: ALT+SHIFT+X

## 플러그인 명령 ID

```
EEID_EXIT_ALL (4119)
```

## 매크로

### \[JavaScript\]

```
editor.ExecuteCommandByID(4119);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4119
```
