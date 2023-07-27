# 선택 범위의 문자 변환 (Ʃ�丮��)

선택 범위 내 문자를 변환하려면, 튜토리얼 매크로에 일곱번째 줄을 추가합니다:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
document.selection.ChangeCase( eeCaseUpperCase );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseUpperCase
위의 매크로를 저장하고 새로운 엠에디터 창에 매크로를 실행합니다.
선택된 텍스트의 문자들이 대문자로 변경된 것을 알 수 있습니다:
TEXT EDITor.
[ChangeCase 메서드](../selection/selectionchangecase) 는
문자를 대문자 또는 소문자로 변환 할 것인지의 여부를 지정하는 인수를 사용합니다.
마찬가지로, 선택 범위 내 문자를 변환하는데 다음의 메서드들이 제공됩니다.
메서드가 사용한 인수에 대한 설명과 같은 더 자세한 내용에 대해서는 각 메서드를 참조하십시오.
|     |     |
| --- | --- |
|[ChangeCase](../selection/selectionchangecase) | 문자를 대문자 또는 소문자로 변환합니다. |
|[ChangeWidth](../selection/selectionchangewidth) | 문자를 반각 문자 또는 전각 문자로 변환합니다. |
|[Format](../selection/selectionformat) | 선택 범위의 줄 바뀜 위치에 새로운 줄을 삽입하거나 새로운 줄을 삭제합니다. |
|[Indent](../selection/selectionindent) | 선택 범위에 의해 지정된 구역을 들여쓰기 합니다. |
|[Tabify](../selection/selectiontabify) | 선택 범위의 공백을 탭으로 변환합니다. |
|[UnIndent](../selection/selectionunindent) | 선택 범위에 의해 지정된 구역을 내어쓰기 합니다. |
|[Untabify](../selection/selectionuntabify) | 선택 범위의 탭을 공백으로 변환합니다. |
```

## 다음 항목:
