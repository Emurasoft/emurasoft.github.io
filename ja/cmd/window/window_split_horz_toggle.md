# \[上下分割の切り替え\] コマンド

## 概要

ウィンドウの上下分割の表示/非表示を切り替えます。

## 説明

ウィンドウが左右に分割されているか、まったく分割されていない場合、このコマンドを実行すると、ウィンドウを中央で上下に分割にして、すぐに分割位置を固定します。
ウィンドウが既に上下に分割されている場合は、上下の分割を解除します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[ウィンドウ\] \- \[分割\] \- \[上下分割の切り替え\]
- ツール バー: ![](../../images/windowsplithorzfix.png)
- ステータス バー: なし
- 既定のショートカット: F12

## プラグイン コマンド ID

```
EEID_WINDOW_SPLIT_HORZ_TOGGLE (4385)
```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4385);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4385
```
