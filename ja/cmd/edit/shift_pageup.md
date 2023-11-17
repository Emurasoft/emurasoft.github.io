# \[選択範囲を1ページ上へ\] コマンド

## 概要

選択範囲を 1 ページ上へ移動します。

## 説明

選択範囲を 1 ページ上へ移動します。プロパティの [\[スクロール\] ページ](../../dlg/properties/scroll/index) で、 **\[半ページ**
**スクロール\]** チェック ボックスがチェックされている場合、半ページだけ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を1ページ上へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Shift+Page Up

## プラグイン コマンド ID

```
EEID_SHIFT_PAGEUP (4178)```

## マクロ

### \[JavaScript\]

```
document.selection.PageUp(true,1);
```

### \[VBScript\]

```
document.selection.PageUp true,1
```
