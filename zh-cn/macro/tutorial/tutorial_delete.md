# 删除字符 (�̳�)

要删除字符，添加第五行到我们所示范的宏中:

#### \[JavaScript\]

> document.selection.Text = "EmEditor supports macros.";
>
> document.selection.NewLine();
>
> document.selection.Text = "\\tEmEditor is a text editor.";
>
> document.selection.CharLeft( false, 12 );
>
> document.selection.DeleteLeft( 15 );

#### \[VBScript\]

> document.selection.Text = "EmEditor supports macros."
>
> document.selection.NewLine
>
> document.selection.Text = Chr(9) & "EmEditor is a text editor."
>
> document.selection.CharLeft False, 12
>
> document.selection.DeleteLeft 15

保存该宏并在一个新的 EmEditor 窗口中运行它。注意，从文本编辑器左边数过来的 15 个字符（即，"(tab)EmEditor is a "）被删除了。EmEditor 会显示如下的文本:

"EmEditor supports macros _."_

"text editor."

**DeleteLeft** **方法** 删除一个字符串左边的指定的字符数。如果被选取的是文本，那被选取的文本会被删除；与在键盘上按 **后退键** 有相同的功能。

同样，下列方法也可以删除字符:

|     |     |
| --- | --- |
| **[Delete](../selection/selection_delete)** | 删除被选取的文本。如果没有选取文本，它会删除一个字符串右边的指定的字符数。等同于 Delete 键。 |
| [**DeleteLeft**](../selection/selection_deleteleft) | 删除被选取的文本。如果没有选取文本，它会删除一个字符串左边的指定的字符数。等同与后退键。 |

你能通过合并方法来删除单词或行:

#### \[JavaScript\]

|     |     |
| --- | --- |
| 删除一个单词。 | document.selection.SelectWord();<br> document.selection.Delete(); |
| 删除光标左边的单词。 | document.selection.WordLeft(true);<br> document.selection.Delete(); |
| 删除光标右边的单词。 | document.selection.WordRight(true);<br> document.selection.Delete(); |
| 删除一行。 | document.selection.SelectLine();<br> document.selection.Delete(); |
| 删除光标左边的行。 | document.selection.StartOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 删除光标右边的行。 | document.selection.EndOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 删除整个文档。 | document.selection.SelectAll();<br> document.selection.Delete(); |

#### \[VBScript\]

|     |     |
| --- | --- |
| 删除一个单词。 | document.selection.SelectWord<br> document.selection.Delete |
| 删除光标左边的单词。 | document.selection.WordLeft True<br> document.selection.Delete |
| 删除光标右边的单词。 | document.selection.WordRight True<br> document.selection.Delete |
| 删除一行。 | document.selection.SelectLine<br> document.selection.Delete |
| 删除光标左边的行。 | document.selection.StartOfLine True, eeLineLogical<br> document.selection.Delete |
| 删除光标右边的行。 | document.selection.EndOfLine True, eeLineLogical<br> document.selection.Delete |
| 删除整个文档。 | document.selection.SelectAll<br> document.selection.Delete |

## 下一主题:
