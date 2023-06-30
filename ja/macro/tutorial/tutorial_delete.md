# 文字を削除する ()

文字を削除するために、チュートリアルのマクロに次のように 5 行目を追加します。

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

document.selection.CharLeft( false, 12 );

document.selection.DeleteLeft( 15 );

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

document.selection.CharLeft False, 12

document.selection.DeleteLeft 15

上記のマクロを保存して別の EmEditor ウィンドウで実行すると、text editor の左側 15
文字が削除されるので、"(タブ)EmEditor is a "の文字列が削除され、

EmEditor supports macros.

text editor.

の 2 行だけが残るはずです。

DeleteLeft
メソッドは、左側の指定した文字数だけ削除します。この場合は関係ありませんが、もし一部のテキストが選択された状態の場合は、選択範囲を削除する動作になります。つまり、キーボードの
Backspace キーを押すのと同じ動作になります。

同様に削除のために、次のメソッドが用意されています。

|     |     |
| --- | --- |
| [Delete](../selection/selection_delete) | 選択範囲を削除します。選択が空の場合は、右側の指定した文字数だけ削除します。Delete キーに相当。 |
| [DeleteLeft](../selection/selection_deleteleft) | 選択範囲を削除します。選択が空の場合は、左側の指定した文字数だけ削除します。Backspace キーに相当。 |

また、単語や行単位で削除したい場合は、次のようにメソッドを組み合わせて実現することができます。

#### \[JavaScript\]

|     |     |
| --- | --- |
| 単語の削除 | document.selection.SelectWord();<br> document.selection.Delete(); |
| 単語の左削除 | document.selection.WordLeft(true);<br> document.selection.Delete(); |
| 単語の右削除 | document.selection.WordRight(true);<br> document.selection.Delete(); |
| 行全体の削除 | document.selection.SelectLine();<br> document.selection.Delete(); |
| 行の左削除 | document.selection.StartOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 行の右削除 | document.selection.EndOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| 文書全体の削除 | document.selection.SelectAll();<br> document.selection.Delete(); |

#### \[VBScript\]

|     |     |
| --- | --- |
| 単語の削除 | document.selection.SelectWord<br> document.selection.Delete |
| 単語の左削除 | document.selection.WordLeft True<br> document.selection.Delete |
| 単語の右削除 | document.selection.WordRight True<br> document.selection.Delete |
| 行全体の削除 | document.selection.SelectLine<br> document.selection.Delete |
| 行の左削除 | document.selection.StartOfLine True, eeLineLogical<br> document.selection.Delete |
| 行の右削除 | document.selection.EndOfLine True, eeLineLogical<br> document.selection.Delete |
| 文書全体の削除 | document.selection.SelectAll<br> document.selection.Delete |

## 次のトピック