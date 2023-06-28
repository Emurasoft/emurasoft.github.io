# \[単語の削除\] コマンド

### 概要

> カーソル位置の単語を削除します。

### 説明

> カーソル位置に存在する単語を削除します。単語の右側に空白が存在する場合、空白は削除しません。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[単語の削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+Delete

### プラグイン コマンド ID

- EEID\_DELETE\_WORD (4194)

### マクロ

#### \[JavaScript\]

> document.selection.SelectWord();
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.SelectWord
>
> document.selection.Delete 1