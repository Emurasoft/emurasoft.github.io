# \[貼り付け\] コマンド

## 概要

クリップボードの内容を貼り付けます。

## 説明

カーソル位置にクリップボード内のテキストを貼り付けます。通常、この操作の前に [\[コピー\] コマンド](edit_copy)、または
[\[切り取り\] コマンド](edit_cut) によってテキストをクリップボードに保存しておきます。プロパティの [\[基本\] ページ](../../dlg/properties/general/index) で、 \[常にANSIで貼り付け\]
チェック ボックスがチェックされている場合は、 [システム既定エンコード](../../glossary/systemdefaultencoding) で貼り付けを行います。チェックされていない場合は、Unicode
で貼り付けます。

## 実行方法

- 既定のメニュー: \[編集\] \- \[貼り付け\]
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[貼り付け\] \- \[貼り付け\]
- ツール バー: ![](../../images/paste.gif)
- ステータス バー: なし
- 既定のショートカット: Ctrl+V または Shift+Insert

## プラグイン コマンド ID

```
EEID_EDIT_PASTE (4129)```

## マクロ

### \[JavaScript\]

```
document.selection.Paste(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.Paste eeCopyUnicode
```
