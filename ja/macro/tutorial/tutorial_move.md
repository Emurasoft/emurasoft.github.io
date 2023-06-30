# カーソルを移動する ()

カーソルを移動するためには、チュートリアルのマクロに次のように 4 行目を追加します。

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

上記のマクロを保存して別の EmEditor ウィンドウで実行すると、マクロの終了後に、カーソル位置は、最後の行末から 12 個文字左、つまり、"text
editor" の最初の t の文字の位置に来るはずです。

[CharLeft メソッド](../selection/selection_charleft) は、カーソル位置を左に指定した文字数だけ移動することを示しています。 [CharLeft \
メソッド](../selection/selection_charleft) の第 1 引数 (false) は、選択範囲の変更を意味するかどうかを指定しています。つまり、キーボードで、左向き矢印キーを押す時に、Shift
キーを押しながら操作するかどうかを示します。

同様にカーソル位置を移動するために、次のメソッドが用意されています。

|     |     |
| --- | --- |
| [CharLeft](../selection/selection_charleft) | カーソル位置を左に指定した文字数だけ移動します。左矢印キーに相当。 |
| [CharRight](../selection/selection_charright) | カーソル位置を右に指定した文字数だけ移動します。右矢印キーに相当。 |
| [LineDown](../selection/selection_linedown) | カーソル位置を下に指定した行数だけ移動します。下矢印キーに相当。 |
| [LineUp](../selection/selection_lineup) | カーソル位置を上に指定した行数だけ移動します。上矢印キーに相当。 |
| [WordLeft](../selection/selection_wordleft) | カーソル位置を単語の左に移動します。Ctrl + 左矢印キーに相当。 |
| [WordRight](../selection/selection_wordright) | カーソル位置を単語の右に移動します。Ctrl + 右矢印キーに相当。 |
| [PageDown](../selection/selection_pagedown) | 1 ページ下へ移動します。Page Up キーに相当。 |
| [PageUp](../selection/selection_pageup) | 1 ページ上へ移動します。Page Down キーに相当。 |
| [StartOfLine](../selection/selection_startofline) | カーソル位置を行の最初に移動します。Home キーに相当。 |
| [EndOfLine](../selection/selection_endofline) | 現在行の最後に移動します。End キーに相当。 |
| [StartOfDocument](../selection/selection_startofdocument) | カーソル位置を文書の最初に移動します。Ctrl + Home キーに相当。 |
| [EndOfDocument](../selection/selection_endofdocument) | カーソル位置を文書の最後に移動します。Ctrl + End キーに相当。 |
| [GoToBrace](../selection/selection_gotobrace) | 対応するかっこへ移動します。 |

また、次のメソッドは、カーソル位置を指定した行、桁位置に移動します。

|     |     |
| --- | --- |
| [SetActivePoint](../selection/selection_setactivepoint) | カーソル位置を設定します。 |

## 次のトピック