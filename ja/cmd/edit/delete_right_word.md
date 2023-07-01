# \[単語右削除\] コマンド

### 概要

> 単語のカーソルから右を削除します。

### 説明

> カーソル位置に存在する単語のカーソルから右側を削除します。単語の右側に空白が存在する場合、その空白も削除します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[単語右削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Delete

### プラグイン コマンド ID

- EEID\_DELETE\_RIGHT\_WORD (4275)

### マクロ

#### \[JavaScript\]

> document.selection.WordRight(true,1);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.WordRight true,1
>
> document.selection.Delete 1
