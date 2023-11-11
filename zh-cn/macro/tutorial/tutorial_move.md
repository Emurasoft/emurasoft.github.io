# 移动光标 (教程)

要移动光标，如下添加第四行到我们所示范的宏中:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
```
保存该宏并在一个新的 EmEditor 窗口中运行它。注意，光标会被放置在从行尾端向左 12 个字符的地方，也就是 "text editor" 的第一个 't' 字符所在处。
[CharLeft 方法](../selection/selectioncharleft) 能把光标往左移指定的字符数。[CharLeft \
方法](../selection/selectioncharleft) 的第一个参数 (false) 指定是否选择范围会变更。换句话说，它指定你是否想要用 SHIFT 键当你在键盘上按下左箭头键时。
下列方法可以操纵光标移动。
|     |     |
| --- | --- |
|[CharLeft](../selection/selectioncharleft) | 把光标向左移动指定的字符数。等同于左箭头键。 |
|[CharRight](../selection/selectioncharright) | 把光标向右移动指定的字符数。等同于右箭头键。 |
|[LineDown](../selection/selectionlinedown) | 把光标向下移动指定的字符数。等同于下移箭头键。 |
|[LineUp](../selection/selectionlineup) | 把光标向上移动指定的字符数。等同于上移箭头键。 |
|[WordLeft](../selection/selectionwordleft) | 把光标往左移一个单词。等同于 CTRL + 左箭头键。 |
|[WordRight](../selection/selectionwordright) | 把光标往右移一个单词。等同于 CTRL + 右箭头键。 |
|[PageDown](../selection/selectionpagedown) | 把光标下移一页。等同于向下翻页键。 |
|[PageUp](../selection/selectionpageup) | 把光标上移一页。等同于 the PAGE UP key. |
|[StartOfLine](../selection/selectionstartofline) | 把光标移到行的起始位置。等同于 HOME 键。 |
|[EndOfLine](../selection/selectionendofline) | 把光标移到行的结尾位置。等同于 END 键。 |
|[StartOfDocument](../selection/selectionstartofdocument) | 把光标移到文档的开始。等同于 CTRL+ HOME。 |
|[EndOfDocument](../selection/selectionendofdocument) | 把光标移到文档的结尾。等同于 CTRL+ END。 |
|[GoToBrace](../selection/selectiongotobrace) | 把光标移到匹配的括号处。 |

下列方法移动光标到到指定的行或数位。
|     |     |
| --- | --- |
|[SetActivePoint](../selection/selectionsetactivepoint) | 设置光标位置。 |
