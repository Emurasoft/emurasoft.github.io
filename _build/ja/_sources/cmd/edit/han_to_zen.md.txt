# \[全角に変換\] コマンド

### 概要

> 選択範囲を全角に変換します。

### 説明

> 選択範囲に存在する半角文字を全角文字に変換します。例えば、A (半角) は Ａ (全角) に、ｱ （半角) は ア (全角) に変換します。

### 実行方法

- 既定のメニュー: \[変換\] \- \[全角に変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[全角に変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_HAN\_TO\_ZEN (4152)

### マクロ

#### \[JavaScript\]

> document.selection.ChangeWidth(eeWidthFullWidth \| eeWidthAllTypes);

#### \[VBScript\]

> document.selection.ChangeWidth eeWidthFullWidth Or eeWidthAllTypes