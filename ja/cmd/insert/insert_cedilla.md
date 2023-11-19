# \[セディーユを挿入\] コマンド

## 概要

c, C を続けてセディーユ付文字を挿入します。

## 説明

カーソル位置に c, C を続けてセディーユ付文字 ç Ç を挿入します。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[発音区別符号\] \- \[セディーユ\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[発音区別符号\] \- \[セディーユ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+,

## プラグイン コマンド ID

```
EEID_INSERT_CEDILLA (4310)

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4310);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4310
```