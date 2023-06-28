\[変換\] \- \[行の分割\]\[変換\] \- \[行の分割\]\[変換\] \- \[行の分割\]

コマンド: \[行の分割\] コマンド

#### [EmEditor ホーム](https://jp.emeditor.com/) - [EmEditor ヘルプ](../../index) \- [コマンド リファレンス](../index)  \- [\[変換\] カテゴリ](../convert/index)

# \[行の分割\] コマンド

### 概要

> 改行コードを挿入して最後のスペースを削除することにより行を分割します。

### 説明

> 選択範囲の行の最初に改行コードを挿入します。 [\[改行コードを挿入\] コマンド](insert_cr_wrap) に似ていますが、改行コード前の空白文字を削除します。改行コードは、その行で使用されている改行コードと一致します。

### 実行方法

- 既定のメニュー: \[変換\] \- \[行の分割\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[行の分割\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_SPLIT\_LINES (4379)

### マクロ

#### \[JavaScript\]

> document.selection.Format(eeFormatSplitLines);

#### \[VBScript\]

> document.selection.Format eeFormatSplitLines