# \[選択範囲を論理行の行頭へ\] コマンド

### 概要

> 選択範囲を論理行の行頭へ移動します。

### 説明

> 選択範囲を論理行の行頭へ移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を論理行の行頭へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+Shift+Home

### プラグイン コマンド ID

- EEID\_SHIFT\_LOGICAL\_HOME (4181)

### マクロ

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineLogical);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineLogical