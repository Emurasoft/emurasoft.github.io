# \[前の文字列を検索\] コマンド

### 概要

> 前のカーソル位置の文字列を検索します。

### 説明

> 文字列が選択されている場合、その文字列を上方向に検索します。文字列が選択されていない場合、カーソル位置の単語を上方向に検索します。

### 実行方法

- 既定のメニュー: \[検索\] \- \[前の文字列を検索\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[前の文字列を検索\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+F3

### プラグイン コマンド ID

- EEID\_FIND\_PREV\_WORD (4205)

### マクロ

#### \[JavaScript\]

> document.selection.FindRepeat(eeFindRepeatPrevious \| eeFindRepeatWord);

#### \[VBScript\]

> document.selection.FindRepeat eeFindRepeatPrevious Or eeFindRepeatWord
