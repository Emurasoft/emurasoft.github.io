# \[次を検索\] コマンド

### 概要

> 次を検索します。

### 説明

> 前回検索した文字列を再び同一条件で下の方向に検索します。

### 実行方法

- 既定のメニュー: \[検索\] \- \[次を検索\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[次を検索\]
- ツール バー: ![](../../images/editrepeat.gif)
- ステータス バー: なし
- 既定のショートカット: F3

### プラグイン コマンド ID

- EEID\_EDIT\_REPEAT (4202)

### マクロ

#### \[JavaScript\]

> document.selection.FindRepeat(eeFindRepeatNext);

#### \[VBScript\]

> document.selection.FindRepeat eeFindRepeatNext