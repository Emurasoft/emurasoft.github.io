# 홈 또는 텍스트 시작점 명령

## 요약

현재 줄의 공백이 아닌 첫 문자로 커서를 이동합니다.

## 설명

현재 줄의 공백이 아닌 첫 문자로 커서를 이동합니다.
이 명령은 현재 행의 시작점의 공백을 무시하고 커서를 공백이 아닌 첫 문자 옆으로 이동합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>가로로 커서 이동 > 홈 또는 텍스트 시작점
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: HOME

## 플러그인 명령 ID

```
EEID_HOME_TEXT (4296)```

## 매크로

### \[JavaScript\]

```
document.selection.StartOfLine(false,eeLineView \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine false,eeLineView \| eeLineHomeText
```
