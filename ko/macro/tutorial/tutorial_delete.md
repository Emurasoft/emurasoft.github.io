# 문자 삭제 (Ʃ�丮��)

문자를 삭제하려면, 튜토리얼 매크로에 다섯번째 줄을 추가합니다:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
위의 매크로를 저장하고 새로운 엠에디터 창에 매크로를 실행합니다.
text editor로부터 왼쪽으로 15문자 (즉, "(tab)EmEditor is a ")가 삭제된 것을 알 수 있습니다.
텍스트는 이제 다음과 같이 보여집니다:
"EmEditor supports macros ."
"text editor."
DeleteLeft메서드 는 문자열의 왼쪽으로 지정된 숫자의 문자 만큼 삭제합니다.
텍스트가 선택되었다면, 선택된 텍스트는 삭제됩니다; 키보드에서백 스페이스 키를 누르면
동일한 효과를 나타냅니다.
마찬가지로, 다음의 메서드들은 문자를 삭제하는데 제공됩니다:
|     |     |
| --- | --- |
|[Delete](../selection/selectiondelete) | 선택된 텍스트를 삭제합니다. 선택된 텍스트가 없는 경우, 문자열의 오른쪽으로 지정된 숫자만큼의<br> 문자를 삭제합니다. Delete에 해당합니다. |
| [DeleteLeft](../selection/selectiondeleteleft) | 선택된 텍스트를 삭제합니다. 선택된 텍스트가 없는 경우, 문자열의 왼쪽으로 지정된 숫자만큼의 문자를<br> 삭제합니다. 백 스페이스 키에 해당합니다. |
메서드들을 결합하여 단어나 줄을 삭제할 수 있습니다:
```

### \[JavaScript\]

```
|     |     |
| --- | --- |
| 한 단어 삭제하기. | document.selection.SelectWord();<br> document.selection.Delete(); |
| 커서 왼쪽의 단어 삭제하기. | document.selection.WordLeft(true);<br> document.selection.Delete(); |
| 커서의 오른쪽의 단어 삭제하기. | document.selection.WordRight(true);<br> document.selection.Delete(); |
| 한 줄 삭제하기. | document.selection.SelectLine();<br> document.selection.Delete(); |
| 왼쪽 줄 삭제하기. | document.selection.StartOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 오른쪽 줄 삭제하기. | document.selection.EndOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 전체 문서 삭제하기. | document.selection.SelectAll();<br> document.selection.Delete(); |
```

### \[VBScript\]

```
|     |     |
| --- | --- |
| 한 단어 삭제하기. | document.selection.SelectWord<br> document.selection.Delete |
| 커서 왼쪽의 단어 삭제하기. | document.selection.WordLeft True<br> document.selection.Delete |
| 커서의 오른쪽의 단어 삭제하기. | document.selection.WordRight True<br> document.selection.Delete |
| 한 줄 삭제하기. | document.selection.SelectLine<br> document.selection.Delete |
| 왼쪽 줄 삭제하기. | document.selection.StartOfLine True, eeLineLogical<br> document.selection.Delete |
| 오른쪽 줄 삭제하기. | document.selection.EndOfLine True, eeLineLogical<br> document.selection.Delete |
| 전체 문서 삭제하기. | document.selection.SelectAll<br> document.selection.Delete |
```

## 다음 항목:
