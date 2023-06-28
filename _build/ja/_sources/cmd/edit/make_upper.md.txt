# \[大文字に変換\] コマンド

### 概要

> 選択範囲を大文字に変換します。

### 説明

> 選択範囲に存在する小文字を大文字に変換します。例えば、a は A に、ａ (全角) は Ａ (全角) に、ä は Ä に、λ は Λ に変換されます。

### 実行方法

- 既定のメニュー: \[変換\] \- \[大文字に変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[大文字に変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+U

### プラグイン コマンド ID

- EEID\_MAKE\_UPPER (4149)

### マクロ

#### \[JavaScript\]

> document.selection.ChangeCase(eeCaseUpperCase);

#### \[VBScript\]

> document.selection.ChangeCase eeCaseUpperCase