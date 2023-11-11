# 매크로 편집 (튜토리얼)

엠에디터는 자동으로 마지막으로 사용된 매크로를 기본 매크로로 만듭니다.
기본 매크로를 편집하려면, [**매크로 편집** 명령](../../cmd/macros/macro_edit) 을
선택합니다. 그 매크로는 엠에디터의 새로운 창에서 열립니다.
기본값이 아닌 매크로를 열고 싶은 경우, [**매크로 선택**\
명령](../../cmd/macros/macro_select) 을 선택하고 편집하기 원하는 매크로를 선택합니다.
이 작업은 그 매크로를 기본값으로 설정합니다.
이제, [**매크로 편집** 명령](../../cmd/macros/macro_edit) 을 선택하여
매크로를 편집할 수 있습니다. 이 튜토리얼에서는, tutorial.jsee 또는 tutorial.vbee을 편집합니다.
그 파일 중 하나를 열었을 때, 다음과 같은 텍스트가 나타납니다:

## 

### \[JavaScript\]

```
document.selection.Text="EmEditor supports macros.";
```

### \[VBScript\]

```
document.selection.Text="EmEditor supports macros."
```
위의 코드는[Text 속성](../selection/selectiontext) 을 사용하고 엠에디터의
현재 커서 위치에 "엠에디터는 매크로를 지원합니다 ." 라는 텍스트를 삽입하도록 합니다.
