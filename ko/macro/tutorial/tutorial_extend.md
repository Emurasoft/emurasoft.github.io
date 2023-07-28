# 선택 범위 변경 (튜토리얼)

선택 범위를 변경하려면, 튜토리얼 매크로에 여섯번째 줄을 추가합니다:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
위의 매크로를 저장하고 새로운 엠에디터 창에 매크로를 실행합니다.
"text edit" 부분이 아래와 같이 강조 표시되어 나타나는 것을 알 수 있습니다:
text editor.
커서를 이동하는 것 뿐만 아니라 선택 범위도 변경한
CharRight 메서드 의 첫번째 매개 변수에 true 를 전합니다; SHIFT 키를 누른 상태에서
오른쪽 화살표 키를 누르면 동일한 효과를 제공합니다.
마찬가지로, 커서를 이동하는 대부분의 메서드는 선택 범위를 변경하려면 인수를 받습니다.
( [커서 이동](tutorialmove) 을 참고합니다).
선택 범위를 변경하는데 더 많은 메서드가 가능합니다:
|     |     |
| --- | --- |
|[SelectAll](../selection/selectionselectall) | 전체 텍스트를 선택합니다. CTRL + A 키에 해당합니다. |
|[SelectLine](../selection/selectionselectline) | 커서가 위치한 줄을 선택합니다. |
|[SelectWord](../selection/selectionselectword) | 커서의 전체 단어를 선택합니다. |
|[Collapse](../selection/selectioncollapse) | 현재 옵션을 해제합니다. ESC에 해당합니다. |
다음의 속성으로 선택 범위의 상태를 설정하거나 확인할 수 있습니다:
|     |     |
| --- | --- |
|[IsActiveEndGreater](../selection/selectionisactiveendgreater) | 활성 지점이 선택 범위의 마지막 부분과 일치하는지 여부를 보여줍니다. |
|[IsEmpty](../selection/selectionisempty) | 선택 범위가 비어 있는지 여부를 보여줍니다. |
|[Mode](../selection/selectionmode) | 선택 유형(수직 선택, 줄 선택 등)을 얻거나 설정합니다. |
```

## 다음 항목:
