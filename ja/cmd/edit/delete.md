# \[削除\] コマンド

### 概要

> 選択範囲またはカーソル上の文字を 1 文字削除します。

### 説明

> 選択範囲が存在する場合はその選択範囲を削除し、ない場合はカーソルの右 1 文字を削除します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[右を1文字削除\]
- ツール バー: ![](../../images/delete.gif)
- ステータス バー: なし
- 既定のショートカット: Shift+Backspace または Delete

### プラグイン コマンド ID

- EEID\_DELETE (4135)

### マクロ

#### \[JavaScript\]

> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.Delete 1
