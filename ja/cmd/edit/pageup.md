# \[1ページ上へ\] コマンド

## 概要

1 ページ上へ移動します。

## 説明

カーソル位置を 1 ページ上へ移動します。プロパティの [\[スクロール\] ページ](../../dlg/properties/scroll/index) で、 **\[半ページ**
**スクロール\]** チェック ボックスがチェックされている場合、半ページだけ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[垂直にカーソル移動\] \- \[1ページ上へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Page Up

## プラグイン コマンド ID

```
EEID_PAGEUP (4162)```

## マクロ

### \[JavaScript\]

```
document.selection.PageUp(false,1);
```

### \[VBScript\]

```
document.selection.PageUp false,1
```
