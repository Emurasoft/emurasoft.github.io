# \[選択範囲を1ページ下へ\] コマンド

## 概要

選択範囲を 1 ページ下へ移動します。

## 説明

選択範囲を 1 ページ下へ移動します。プロパティの [\[スクロール\] ページ](../../dlg/properties/scroll/index) で、\[半ページ
スクロール\] チェック ボックスがチェックされている場合、半ページだけ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を1ページ下へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Shift+Page Down

## プラグイン コマンド ID

```
EEID_SHIFT_PAGEDOWN (4179)```

## マクロ

### \[JavaScript\]

```
document.selection.PageDown(true,1);
```

### \[VBScript\]

```
document.selection.PageDown true,1
```
