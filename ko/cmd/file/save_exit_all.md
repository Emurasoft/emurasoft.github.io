# 저장 후 모두 닫기 명령

## 요약

열려있는 모든 파일을 저장 후 닫습니다.

## 설명

열려있는 모든 파일을 저장 후 닫습니다.
이 명령은 [**모두 저장** 명령](file_save_all) 후에 [**모두 닫기** 명령](exit_all) 을 실행 한 것과
동일시 작용됩니다.

## 실행하는 방법

- 기본 메뉴: **파일** \> **저장 후 모두 닫기**
- [모든 명령](../tools/all_commands): **파일** \> **닫기**
\> **저장 후 모두 닫기**
- 도구 모음: ![](../../images/saveexitall.png)
- 상태 표시줄: 없음
- 기본 바로 가기 키: CTRL+SHIFT+E

## 플러그인 명령 ID

```
EEID_SAVE_EXIT_ALL (4118)
```

## 매크로

## \[JavaScript\]

```
editor.ExecuteCommandByID(4118);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4118
```
