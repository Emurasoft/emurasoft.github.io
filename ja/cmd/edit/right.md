# \[1文字右へ\] コマンド

### 概要

> 1 文字右へ移動します。

### 説明

> カーソル位置を 1 文字右へ移動します。カーソル位置が行末の場合、次の行の先頭に移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[1文字右へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Right

### プラグイン コマンド ID

- EEID\_RIGHT (4156)

### マクロ

#### \[JavaScript\]

> document.selection.CharRight(false,1);

#### \[VBScript\]

> document.selection.CharRight false,1
