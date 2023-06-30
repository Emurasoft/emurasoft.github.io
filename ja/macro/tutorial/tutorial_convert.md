# 選択範囲の文字を変換する ()

選択範囲の文字を変換するために、チュートリアルのマクロに、次のように 7 行目を追加します。

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

document.selection.CharLeft( false, 12 );

document.selection.DeleteLeft( 15 );

document.selection.CharRight( true, 9 );

document.selection.ChangeCase( eeCaseUpperCase );

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

document.selection.CharLeft False, 12

document.selection.DeleteLeft 15

document.selection.CharRight True, 9

document.selection.ChangeCase eeCaseUpperCase

上記のマクロを保存して別の EmEditor ウィンドウで実行すると、選択されたテキストが大文字に変換され、

TEXT EDITor.

と表示されます。 [ChangeCase メソッド](../selection/selection_changecase) には、1
個の引数を受け取り、大文字に変換するか、小文字に変換するかを指定することができます。

同様に選択範囲の文字を変換するために、次のメソッドが用意されています。メソッドが受け取る引数など詳しくは、それぞれのメソッドの説明を参照してください。

|     |     |
| --- | --- |
| [ChangeCase](../selection/selection_changecase) | 選択されたテキストの大文字と小文字を変換します。 |
| [ChangeWidth](../selection/selection_changewidth) | 半角文字と全角文字を変換します。 |
| [Format](../selection/selection_format) | 選択範囲の折り返し位置に改行コードの挿入したり、改行コードを削除したりします。 |
| [Indent](../selection/selection_indent) | 選択範囲をインデントします。 |
| [Tabify](../selection/selection_tabify) | 選択範囲の空白を Tab に変換します。 |
| [UnIndent](../selection/selection_unindent) | 選択範囲の逆インデントを行います。 |
| [Untabify](../selection/selection_untabify) | 選択範囲の Tab を空白に移動します。 |

## 次のトピック