# \[行の2重化\] コマンド

## 概要

カーソルのある論理行全体を 2 重化します。

## 説明

カーソルのある論理行とのコピーを作成し、カーソル行の下に挿入します。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[行の2重化\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[行の2重化\]
- ツール バー: ![](../../images/duplicateline..png)
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+Y

## プラグイン コマンド ID

```
EEID_DUPLICATE_LINE (4328)
```

## マクロ

### \[JavaScript\]

```
document.selection.DuplicateLine();
```

### \[VBScript\]

```
document.selection.DuplicateLine
```
