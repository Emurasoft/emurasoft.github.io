# 選択範囲を変更する (チュートリアル)

選択範囲を変更するために、チュートリアルのマクロに、次のように 6 行目を追加します。

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
上記のマクロを保存して別の EmEditor ウィンドウで実行すると、
text editor.
のように、text edit の部分が選択されて表示されます。
CharRight メソッドの第 1 引数に true
を指定したため、単にカーソルを移動するだけでなく、選択範囲も変更することを示しています。つまり、キーボードの Shift
キーを押しながら右向き矢印キーを押すことを示しています。
同様にカーソル位置を移動するためのほとんどメソッドで、選択範囲を変更する引数が利用できます ( [カーソルを移動する](tutorialmove) を参照してください)。
その他、選択範囲を変更するために、次のメソッドが用意されています。
|     |     |
| --- | --- |
| [SelectAll](../selection/selectionselectall) | 開いている文書の全体を選択します。Ctrl + A に相当。 |
| [SelectLine](../selection/selectionselectline) | カーソル位置の行を選択します。 |
| [SelectWord](../selection/selectionselectword) | カーソル位置の単語を選択します。 |
| [Collapse](../selection/selectioncollapse) | 選択を解除します。Esc キーに相当。 |
また、次のプロパティで、選択範囲の状態を調べたり設定することができます。
|     |     |
| --- | --- |
| [IsActiveEndGreater](../selection/selectionisactiveendgreater) | アクティブ ポイントが選択範囲の下部と一致しているかどうかを示します。 |
| [IsEmpty](../selection/selectionisempty) | 選択範囲が空かどうかを示します。 |
| [Mode](../selection/selectionmode) | 選択の種類 (箱型選択、行選択など) を取得、または設定します。 |
```

## 次のトピック
