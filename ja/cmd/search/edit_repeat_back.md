# \[前を検索\] コマンド

### 概要

> 前を検索します。

### 説明

> 前回検索した文字列を再び同一条件で上の方向に検索します。

### 実行方法

- 既定のメニュー: \[検索\] \- \[前を検索\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[前を検索\]
- ツール バー:
![](../../images/editrepeatback.gif)
- ステータス バー: なし
- 既定のショートカット: Shift+F3

### プラグイン コマンド ID

- EEID\_EDIT\_REPEAT\_BACK (4203)

### マクロ

#### \[JavaScript\]

> document.selection.FindRepeat(eeFindRepeatPrevious);

#### \[VBScript\]

> document.selection.FindRepeat eeFindRepeatPrevious
