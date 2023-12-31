# \[引用付きコピー\] コマンド

## 概要

選択範囲を引用マークを付けてコピーしてクリップボードに保存します。

## 説明

選択されたテキストを行の最初に引用マークを付けてコピーして、その内容をクリップボードに保存します。この操作の後、別の場所にカーソルを移動して
[\[貼り付け\] コマンド](edit_paste) を実行することにより、コピーしたテキストを別の場所にコピーすることができます。

## 実行方法

- 既定のメニュー: \[編集\] \- \[引用付きコピー\]
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[コピー\] \- \[引用付きコピー\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Q

## プラグイン コマンド ID

```
EEID_EDIT_COPY_PREFIX (4130)```

## マクロ

### \[JavaScript\]

```
document.selection.Copy(eeCopyQuotes);
```

### \[VBScript\]

```
document.selection.Copy eeCopyQuotes
```
