# \[単語左削除\] コマンド

### 概要

> 単語のカーソルから左を削除します。

### 説明

> カーソル位置に存在する単語のカーソルから左側を削除します。単語の左側に空白が存在する場合、その空白は削除しません。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[単語左削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Backspace

### プラグイン コマンド ID

- EEID\_DELETE\_LEFT\_WORD (4280)

### マクロ

#### \[JavaScript\]

> document.selection.WordLeft(true,1);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.WordLeft true,1
>
> document.selection.Delete 1