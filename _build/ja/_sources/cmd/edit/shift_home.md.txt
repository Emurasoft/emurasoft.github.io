# \[選択範囲を行頭へ\] コマンド

### 概要

> 選択範囲を行頭へ移動します。

### 説明

> 選択範囲を表示行の行頭へ移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を行頭へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Shift+Home

### プラグイン コマンド ID

- EEID\_SHIFT\_HOME (4180)

### マクロ

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineView);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineView