# \[コピー\] コマンド

## 概要

選択範囲をコピーしてクリップボードに保存します。

## 説明

選択されたテキストをコピーして、その内容をクリップボードに保存します。この操作の後、別の場所にカーソルを移動して
[\[貼り付け\] コマンド](edit_paste) を実行することにより、コピーしたテキストをコピーすることができます。

## 実行方法

- 既定のメニュー: \[編集\] \- \[コピー\]
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[コピー\] \- \[コピー\]
- ツール バー: ![](../../images/copy.png)
- ステータス バー: なし
- 既定のショートカット: Ctrl+C または Ctrl+Insert

## プラグイン コマンド ID

```
EEID_EDIT_COPY (4127)
```

## マクロ

### \[JavaScript\]

```
document.selection.Copy(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.Copy eeCopyUnicode
```
