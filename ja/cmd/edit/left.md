# \[1文字左へ\] コマンド

### 概要

> 1 文字左へ移動します。

### 説明

> カーソル位置を 1 文字左へ移動します。カーソル位置が行頭の場合、前の行の行末に移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[1文字左へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Left

### プラグイン コマンド ID

- EEID\_LEFT (4157)

### マクロ

#### \[JavaScript\]

> document.selection.CharLeft(false,1);

#### \[VBScript\]

> document.selection.CharLeft false,1
