# \[引用と改行コード付き貼り付け\] コマンド

## 概要

クリップボードの内容に引用マークと改行コードを付けて貼り付けます。

## 説明

カーソル位置にクリップボード内のテキストを貼り付けます。この際、折り返し位置に改行コードと引用マークを挿入します。通常、この操作の前に [\[コピー\] コマンド](edit_copy)、または [\[切り取り\] コマンド](edit_cut) によってテキストをクリップボードに保存しておきます。プロパティの

[\[基本\] タブ](../../dlg/properties/general/index) で、\[常にANSIで貼り付け\] チェック ボックスがチェックされている場合は、 [システム既定エンコード](../../glossary/systemdefaultencoding) で貼り付けを行います。チェックされていない場合は、Unicode
で貼り付けます。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[貼り付け\] \- \[引用と改行コード付き貼り付け\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_PASTE_PREFIX_RETURN (4134)```

## マクロ

### \[JavaScript\]

```
document.selection.Paste(eeCopyQuotes \| eeCopyNL);
```

### \[VBScript\]

```
document.selection.Paste eeCopyQuotes Or eeCopyNL
```
