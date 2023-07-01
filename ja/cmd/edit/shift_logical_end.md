# \[選択範囲を論理行の行末へ\] コマンド

### 概要

> 選択範囲を論理行の行末へ移動します。

### 説明

> 選択範囲を論理行の行末へ移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を論理行の行末へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+Shift+End

### プラグイン コマンド ID

- EEID\_SHIFT\_LOGICAL\_END (4183)

### マクロ

#### \[JavaScript\]

> document.selection.EndOfLine(true,eeLineLogical);

#### \[VBScript\]

> document.selection.EndOfLine(true,eeLineLogical);
