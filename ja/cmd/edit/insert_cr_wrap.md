# \[改行コードを挿入\] コマンド

### 概要

> 選択範囲の各行の折り返し位置に改行コードを挿入します。

### 説明

> 選択範囲の行の最初に改行コードを挿入します。改行コード前の空白文字は削除しません。改行コードは、その行で使用されている改行コードと一致します。

### 実行方法

- 既定のメニュー: \[変換\] \- \[改行コードを挿入\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[改行コードを挿入\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_INSERT\_CR\_WRAP (4143)

### マクロ

#### \[JavaScript\]

> document.selection.Format(eeFormatInsertNL);

#### \[VBScript\]

> document.selection.Format eeFormatInsertNL