# \[CSV (複数項目)\] コマンド

### 概要

> 文書を指定するCSVとして表示します (複数項目)。

### 説明

> 文書を指定するCSVとして表示します。

### 実行方法

- 既定のメニュー: \[CSV\] - (CSV)
- [すべてのコマンド](../../glossary/allcommands): \[CSV\] - (CSV)
- ツール バー: ![](../../images/csv_mode.gif) (CSV)
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_SV\_MODE から EEID\_SV\_MODE + 63 まで (22528 から 22528 + 63 まで)

### マクロ

#### \[JavaScript\]

> editor.ExecuteCommandByID(22528 + i);  // i は 0 から 63 までの整数

#### \[VBScript\]

> editor.ExecuteCommandByID 22528 + i  ' i は 0 から 63 までの整数