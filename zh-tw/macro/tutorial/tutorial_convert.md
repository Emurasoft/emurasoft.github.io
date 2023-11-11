# 在選取範圍內轉換字元 (教程)

要在選取範圍內轉換字元，添加第七行到我們所示范的巨集中:

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
```

儲存該巨集并在一個新的 EmEditor 視窗中運行它。注意，所選取的文字的字元已被轉換為大寫:
TEXT EDITor.
[ChangeCase 方法](../selection/selection_changecase) 接受一個參數，這個參數指定
字元是要被轉換為大寫還是小寫。
同樣，下列方法也能在選取範圍內轉換字元。更多信息，例如有關方法所接受的參數的說明等等，請參考每一個方法。
|     |     |
| --- | --- |
|[ChangeCase](../selection/selection_changecase) | 把字元轉換為大寫或小寫。 |
|[ChangeWidth](../selection/selection_changewidth) | 把字元轉換為全形或半形。 |
|[Format](../selection/selection_format) | 在選取範圍內的一個換行位置處插入或刪除一個新行。 |
|[Indent](../selection/selection_indent) | 縮排由選取範圍指定的部分。 |
|[Tabify](../selection/selection_tabify) | 在選取範圍內把空白轉換為 tab。 |
|[UnIndent](../selection/selection_unindent) | 取消縮排由選取範圍指定的部分。 |
|[Untabify](../selection/selection_untabify) | 在選取範圍內把 tab 轉換為空白。 |
