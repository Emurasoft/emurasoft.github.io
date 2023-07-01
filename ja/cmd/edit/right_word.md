# \[1単語右へ\] コマンド

### 概要

> 1 単語右へ移動します。

### 説明

> カーソル位置を 1 単語右へ移動します。単語の右側に空白が存在する場合、空白を超えて次の単語の先頭に移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[1単語右へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Right

### プラグイン コマンド ID

- EEID\_RIGHT\_WORD (4158)

### マクロ

#### \[JavaScript\]

> document.selection.WordRight(false,1);

#### \[VBScript\]

> document.selection.WordRight false,1
