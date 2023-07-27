# \[下に行挿入\] コマンド

## 概要

カーソル位置の下に行を挿入します。

## 説明

カーソル位置の下に空の 1 行を挿入します。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[下に空行\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[下に空行\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+Enter

## プラグイン コマンド ID

```
EEID_LINE_OPEN_BELOW (4196)```

## マクロ

### \[JavaScript\]

```
document.selection.LineOpen(false);
```

### \[VBScript\]

```
document.selection.LineOpen false
```
