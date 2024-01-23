# 在选取范围内转换字符 (教程)

要在选取范围内转换字符，添加第七行到我们所示范的宏中:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\tEmEditor is a text editor.";
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

保存该宏并在一个新的 EmEditor 窗口中运行它。注意，所选取的文本的字符已被转换为大写:
TEXT EDITor.
[ChangeCase 方法](../selection/selection_changecase) 接受一个参数，这个参数指定
字符是要被转换为大写还是小写。
同样，下列方法也能在选取范围内转换字符。更多信息，例如有关方法所接受的参数的说明等等，请参考每一个方法。
|     |     |
| --- | --- |
|[ChangeCase](../selection/selection_changecase) | 把字符转换为大写或小写。 |
|[ChangeWidth](../selection/selection_changewidth) | 把字符转换为全角或半角。 |
|[Format](../selection/selection_format) | 在选取范围内的一个换行位置处插入或删除一个新行。 |
|[Indent](../selection/selection_indent) | 缩进由选取范围指定的部分。 |
|[Tabify](../selection/selection_tabify) | 在选取范围内把空格转换为 tab。 |
|[UnIndent](../selection/selection_unindent) | 取消缩进由选取范围指定的部分。 |
|[Untabify](../selection/selection_untabify) | 在选取范围内把 tab 转换为空格。 |
