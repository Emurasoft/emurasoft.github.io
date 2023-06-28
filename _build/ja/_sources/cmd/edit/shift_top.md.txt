# \[選択範囲を文頭へ\] コマンド

### 概要

> 選択範囲を文頭へ移動します。

### 説明

> 選択範囲を文頭へ移動します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を文頭へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+Home

### プラグイン コマンド ID

- EEID\_SHIFT\_TOP (4184)

### マクロ

#### \[JavaScript\]

> document.selection.StartOfDocument(true);

#### \[VBScript\]

> document.selection.StartOfDocument true