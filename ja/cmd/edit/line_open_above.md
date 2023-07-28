# \[上に行挿入\] コマンド

## 概要

カーソル位置の上に行を挿入します。

## 説明

カーソル位置の上に空の 1 行を挿入します。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[上に空行\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[上に空行\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Shift+Enter

## プラグイン コマンド ID

```
EEID_LINE_OPEN_ABOVE (4195)```

## マクロ

### \[JavaScript\]

```
document.selection.LineOpen(true);
```

### \[VBScript\]

```
document.selection.LineOpen true
```
