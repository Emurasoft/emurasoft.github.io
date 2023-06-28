# \[左を1文字削除\] コマンド

### 概要

> 選択範囲またはカーソルの左を 1 文字削除します。

### 説明

> 選択範囲が存在する場合はその選択範囲を削除し、ない場合はカーソルの左 1 文字を削除します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[左を1文字削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Backspace

### プラグイン コマンド ID

- EEID\_BACK (4186)

### マクロ

#### \[JavaScript\]

> document.selection.DeleteLeft(1);

#### \[VBScript\]

> document.selection.DeleteLeft 1