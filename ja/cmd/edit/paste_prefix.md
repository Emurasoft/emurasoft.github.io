# \[引用付き貼り付け\] コマンド

## 概要

クリップボードの内容に引用マークを付けて貼り付けます。

## 説明

カーソル位置にクリップボード内のテキストを行頭に引用マークを付けて貼り付けます。通常、この操作の前に
[\[コピー\] コマンド](edit_copy)、または [\[切り取り\] コマンド](edit_cut) によってテキストをクリップボードに保存しておきます。プロパティの [**\[基本\]** タブ](../../dlg/properties/general/index) で、 **\[常にANSIで貼り付け\]**
チェック ボックスがチェックされている場合は、 [システム既定エンコード](../../glossary/systemdefaultencoding) で貼り付けを行います。チェックされていない場合は、Unicode
で貼り付けます。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[貼り付け\] \- \[引用付き貼り付け\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+B

## プラグイン コマンド ID

```
EEID_PASTE_PREFIX (4132)```

## マクロ

### \[JavaScript\]

```
document.selection.Paste(eeCopyQuotes);
```

### \[VBScript\]

```
document.selection.Paste eeCopyQuotes
```
