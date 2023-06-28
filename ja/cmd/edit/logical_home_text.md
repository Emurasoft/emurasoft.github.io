# \[論理行の行頭またはテキスト開始へ\] コマンド

### 概要

> 論理行の行頭またはテキスト開始位置へ移動します。

### 説明

> カーソル位置を論理行の行頭へ移動します。ただし、行頭に空白が存在する場合で、現在のカーソル位置が空白を除いたテキストの開始位置でない場合、その空白を除いたテキストの開始位置に移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\]
\- \[論理行の行頭またはテキスト開始へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_LOGICAL\_HOME\_TEXT (4333)

### マクロ

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineLogical \| eeLineHomeText);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineLogical Or eeLineHomeText