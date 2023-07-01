# \[選択範囲の空白をタブに変換\] コマンド

### 概要

> 選択範囲の空白をタブに変換します。

### 説明

> 選択範囲に存在する行頭の空白文字をタブに変換します。タブの桁数については、プロパティの
> [**\[基本\]** タブ](../../dlg/properties/general/index) の
>
> **\[タブ/インデント\]** ボタンをクリックし、 [**\[タブ/インデント\]** ダイアログ ボックス](../../dlg/properties/general/indent/index) で設定できます。

### 実行方法

- 既定のメニュー: \[変換\] \- \[空白をTabに変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[空白をTabに変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_TABIFY (4356)

### マクロ

#### \[JavaScript\]

> document.selection.Tabify();

#### \[VBScript\]

> document.selection.Tabify
