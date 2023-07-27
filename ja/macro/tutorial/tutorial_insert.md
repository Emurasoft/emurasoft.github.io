# 文字を挿入する ()

マクロを使って文字を挿入するには、 [Text プロパティ](../selection/selection_text) を利用します。チュートリアルで保存されたファイルを次のように書き換えてみます。

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
2行目に追加された [NewLine メソッド](../selection/selectionnewline) は、カーソル位置に改行コードを挿入するというものです。また、3行目には、文字列の最初にタブ文字を挿入しています。タブ文字は、JavaScript
では、"\\t" で表現することができ、VBScript では Chr(9) と表記することができます。Chr(9) の代わりに vbTab
という定数を利用することもできます。
以下に、両者のスクリプト言語で利用できる主な定数 (表記) の一覧を説明します。
```

### \[JavaScript\]

```
|     |     |     |
| --- | --- | --- |
| \\b | \\u0008 | バックスペース。 |
| \\t | \\u0009 | 水平タブ。 |
| \\n | \\u000a | 改行。 |
| \\f | \\u000c | フォームフィード。 |
| \\r | \\u000d | 復帰。 |
| \\" | \\u0022 | 2 重引用符 |
| \\' | \\u0027 | 1 重引用符 |
| \\\ | \\u005c | バックスラッシュ |
| \\xXX |  | 2 桁の 16 進数で表記された Latin-1 文字 |
| \\uXXXX |  | 4 桁の 16 進数で表記された Unicode 文字 |
```

### ![](../../images/g.gif) 参考： [JScript \ 特殊文字 (Microsoft MSDN ライブラリ)](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Lexical_grammar\#String_literals)

### \[VBScript\]

```
|     |     |     |
| --- | --- | --- |
| vbCr | Chr(13) | 復帰。 |
| vbCrLf | Chr(13) & Chr(10) | 復帰改行。 |
| vbFormFeed | Chr(12) | フォーム フィード。 |
| vbLf | Chr(10) | 改行。 |
| vbNewLine | Chr(13) & Chr(10) または Chr(10) | プラットフォーム固有の改行コード。Windowsでは vbCrLfと同じです。 |
| vbTab | Chr(9) | 水平タブ |
| vbVerticalTab | Chr(11) | 垂直タブ |
```

### ![](../../images/g.gif) 参考： [VBScript \ 文字列の定数 (Microsoft MSDN ライブラリ)](https://docs.microsoft.com/ja-jp/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/hh277t8e(v=vs.84))

## 注意

復帰改行を表す文字には、\\r (CR) と \\n (LF)
が存在し、これらは厳密に区別する必要があります。例えば、document.selection.Text = "\\n"; とすると、改行文字 (LF)
だけが挿入され復帰文字 (CR) が挿入されないため、Windows の通常のファイルの改行コードと異なります。EmEditor
で改行キーを押したときは、その行で使用されている復帰改行 (CR のみ、LF のみ、または CR+LF) を利用して挿入しています。EmEditor
の改行を押す場合と同じ操作を行いたい場合は、 [NewLine メソッド](../selection/selection_newline) または
[writeln メソッド](../document/document_writeln) を利用することを推奨します。

## 次のトピック
