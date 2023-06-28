# \[改行コードを削除\] コマンド

### 概要

> 選択範囲の各行の折り返し位置の改行コードを削除します。

### 説明

> 選択範囲の行の折り返し位置に存在する改行コードを削除します。 [\[行を結合\] コマンド](join_lines) に似ていますが、改行コード前に空白文字を挿入しません。

### 実行方法

- 既定のメニュー: \[変換\] \- \[改行コードを削除\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[改行コードを削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_DELETE\_CR\_WRAP (4144)

### マクロ

#### \[JavaScript\]

> document.selection.Format(eeFormatDeleteNL);

#### \[VBScript\]

> document.selection.Format eeFormatDeleteNL