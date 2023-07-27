# マクロの編集 ()

[\[マクロの編集\] コマンド](../../cmd/macros/macro_edit) (\[マクロ\] メニューの \[編集\])
を選択すると、既定のマクロがファイルの場合、そのファイルを別の EmEditor ウィンドウから開きます。ここでは、チュートリアルで保存した
tutorial.jsee または tutorial.vbee というファイルを開くことになります。もし、他のマクロ ファイルが既定のファイルの場合は、一度、 [\[マクロの選択\] \
コマンド](../../cmd/macros/macro_select) (\[マクロ\] メニューの \[選択\]) を選択して目的のマクロ ファイルを既定のマクロに変更してから、 [\[マクロの編集\] \
コマンド](../../cmd/macros/macro_edit) (\[マクロ\] メニューの \[編集\]) を選択します。すると、以下のように表示されます。

## 

### \[JavaScript\]

```
document.selection.Text="EmEditor supports macros.";
```

### \[VBScript\]

```
document.selection.Text="EmEditor supports macros."
これは、現在の文書のカーソル位置に "EmEditor supports macros." という文字列を挿入しなさい、という意味になり、 [Text \
プロパティ](../selection/selectiontext) を利用しています。
```

## 次のトピック
