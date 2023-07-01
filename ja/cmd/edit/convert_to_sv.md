# \[CSVに変換 (複数項目)\] コマンド

### 概要

> 現在のCSV文書または固定幅列文書を指定するCSV文書に変換します (複数項目)。

### 説明

> 現在のCSV文書または固定幅列文書を指定するCSV文書に変換します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[CSV\] - \[次のCSVに変換\] - (CSVに変換)
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_CONVERT\_TO\_SV から EEID\_CONVERT\_TO\_SV + 63 まで (22656 から 22656 + 63 まで)

### マクロ

#### \[JavaScript\]

> editor.ExecuteCommandByID(22656 + i);  // i は 0 から 63 までの整数

#### \[VBScript\]

> editor.ExecuteCommandByID 22656  ' i は 0 から 63 までの整数
