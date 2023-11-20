# \[行の結合\] コマンド

## 概要

各行の改行コードを削除して行の最後にスペースを挿入することにより行を結合します。

## 説明

選択範囲の行の折り返し位置に存在する改行コードを削除します。 [\[改行を削除\] コマンド](delete_cr_wrap) に似ていますが、改行コード前に空白文字を挿入します。

## 実行方法

- 既定のメニュー: \[変換\] \- \[行の結合\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[行の結合\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_JOIN_LINES (4378)```

## マクロ

### \[JavaScript\]

```
document.selection.Format(eeFormatJoinLines);
```

### \[VBScript\]

```
document.selection.Format eeFormatJoinLines
```
