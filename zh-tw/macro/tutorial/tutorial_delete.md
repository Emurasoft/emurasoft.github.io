# 刪除字元 (�е{)

要刪除字元，添加第五行到我們所示范的巨集中:

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

儲存該巨集并在一個新的 EmEditor 視窗中運行它。注意，從文字編輯器左邊數過來的 15 個字元 (即，"(tab)EmEditor is a ") 被刪除了。EmEditor 會顯示如下的文字:

"EmEditor supports macros _."_

"text editor."

**DeleteLeft** **方法** 刪除一個字串左邊的指定的字元數。如果被選取的是文字，那被選取的文字會被刪除；與在鍵盤上按 **后退鍵** 有相同的功能。

同樣，下列方法也可以刪除字元:

|     |     |
| --- | --- |
| **[Delete](../selection/selection_delete)** | 刪除被選取的文字。如果沒有選取文字，它會刪除一個字串右邊的指定的字元數。等同于 Delete 鍵。 |
| [**DeleteLeft**](../selection/selection_deleteleft) | 刪除被選取的文字。如果沒有選取文字，它會刪除一個字串左邊的指定的字元數。等同與后退鍵。 |

您能通過合併方法來刪除單字或行:

#### \[JavaScript\]

|     |     |
| --- | --- |
| 刪除一個單字。 | document.selection.SelectWord();<br> document.selection.Delete(); |
| 刪除游標左邊的單字。 | document.selection.WordLeft(true);<br> document.selection.Delete(); |
| 刪除游標右邊的單字。 | document.selection.WordRight(true);<br> document.selection.Delete(); |
| 刪除一行。 | document.selection.SelectLine();<br> document.selection.Delete(); |
| 刪除游標左邊的行。 | document.selection.StartOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 刪除游標右邊的行。 | document.selection.EndOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 刪除整個文檔。 | document.selection.SelectAll();<br> document.selection.Delete(); |

#### \[VBScript\]

|     |     |
| --- | --- |
| 刪除一個單字。 | document.selection.SelectWord<br> document.selection.Delete |
| 刪除游標左邊的單字。 | document.selection.WordLeft True<br> document.selection.Delete |
| 刪除游標右邊的單字。 | document.selection.WordRight True<br> document.selection.Delete |
| 刪除一行。 | document.selection.SelectLine<br> document.selection.Delete |
| 刪除游標左邊的行。 | document.selection.StartOfLine True, eeLineLogical<br> document.selection.Delete |
| 刪除游標右邊的行。 | document.selection.EndOfLine True, eeLineLogical<br> document.selection.Delete |
| 刪除整個文檔。 | document.selection.SelectAll<br> document.selection.Delete |

## 下一主題:
