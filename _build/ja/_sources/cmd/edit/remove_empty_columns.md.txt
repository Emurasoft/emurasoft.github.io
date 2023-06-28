# \[空列を削除\] コマンド

### 概要

> CSV文書から空列を削除します。

### 説明

> CSV文書から空列を削除します。空列とは、列のすべてのセルが空または現在の CSV フォーマットに定義された 2 個の引用符のみ、通常 "" であることを意味します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): なし
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_REMOVE\_EMPTY\_COLUMNS (4062)

### マクロ

#### \[JavaScript\]

> editor.ExecuteCommandByID(4062);

#### \[VBScript\]

> editor.ExecuteCommandByID 4062