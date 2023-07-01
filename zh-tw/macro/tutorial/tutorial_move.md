# 移動游標 (�е{)

要移動游標，如下添加第四行到我們所示范的巨集中:

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

document.selection.CharLeft( false, 12 );

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

document.selection.CharLeft False, 12

儲存該巨集并在一個新的 EmEditor 視窗中運行它。注意，游標會被放置在從行尾端向左 12 個字元的地方，也就是 "text editor" 的第一個 't' 字元所在處。

**[CharLeft 方法](../selection/selection_charleft)** 能把游標往左移指定的字元數。 **[CharLeft \**
**方法](../selection/selection_charleft)** 的第一個參數 (false) 指定是否選擇範圍會變更。換句話說，它指定您是否想要用 SHIFT 鍵當您在鍵盤上按下左箭頭鍵時。

下列方法可以操縱游標移動。

|     |     |
| --- | --- |
| **[CharLeft](../selection/selection_charleft)** | 把游標向左移動指定的字元數。等同于左箭頭鍵。 |
| **[CharRight](../selection/selection_charright)** | 把游標向右移動指定的字元數。等同于右箭頭鍵。 |
| **[LineDown](../selection/selection_linedown)** | 把游標向下移動指定的字元數。等同于下移箭頭鍵。 |
| **[LineUp](../selection/selection_lineup)** | 把游標向上移動指定的字元數。等同于上移箭頭鍵。 |
| **[WordLeft](../selection/selection_wordleft)** | 把游標往左移一個單字。等同于 CTRL + 左箭頭鍵。 |
| **[WordRight](../selection/selection_wordright)** | 把游標往右移一個單字。等同于 CTRL + 右箭頭鍵。 |
| **[PageDown](../selection/selection_pagedown)** | 把游標下移一頁。等同于向下翻頁鍵。 |
| **[PageUp](../selection/selection_pageup)** | 把游標上移一頁。等同于 the PAGE UP key. |
| **[StartOfLine](../selection/selection_startofline)** | 把游標移到行的起始位置。等同于 HOME 鍵。 |
| **[EndOfLine](../selection/selection_endofline)** | 把游標移到行的結尾位置。等同于 END 鍵。 |
| **[StartOfDocument](../selection/selection_startofdocument)** | 把游標移到文檔的開始。等同于 CTRL+ HOME。 |
| **[EndOfDocument](../selection/selection_endofdocument)** | 把游標移到文檔的結尾。等同于 CTRL+ END。 |
| **[GoToBrace](../selection/selection_gotobrace)** | 把游標移到符合的括號處。 |

下列方法移動游標到到指定的行或數位。

|     |     |
| --- | --- |
| **[SetActivePoint](../selection/selection_setactivepoint)** | 設置游標位置。 |

## 下一主題:
