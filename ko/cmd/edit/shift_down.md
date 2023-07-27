# 한 줄 아래까지 선택 명령

## 요약

한 줄 아래까지 선택을 확장합니다.

## 설명

한 줄 아래까지 선택을 확장합니다. 이 명령은 텍스트가 선택되지 않았다면, 직접 커서 위치 아래의 줄을 선택합니다.

## 실행하는 방법

- 기본 메뉴: 없음
- [모든 명령](../tools/all_commands):편집 \>선택 확장 \>한 줄 아래까지 선택
- 도구 모음: 없음
- 상태 표시줄: 없음
- 기본 바로 가기 키: SHIFT+DOWN ARROW

## 플러그인 명령 ID

```
EEID_SHIFT_DOWN (4177)```

## 매크로

### \[JavaScript\]

```
document.selection.LineDown(true,1);
```

### \[VBScript\]

```
document.selection.LineDown true,1
```
