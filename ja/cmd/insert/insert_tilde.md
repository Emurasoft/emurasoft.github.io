# \[ティルデを挿入\] コマンド

## 概要

a, n, o, A, N, O を続けてティルデ付文字を挿入します。

## 説明

カーソル位置に a, n, o, e, u, A, N, O, E, U を続けてティルデ付文字 ã, ñ, õ, ẽ, ũ, Ã, Ñ, Õ, Ẽ, Ũ を挿入します。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[発音区別符号\] \- \[ティルデ\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[発音区別符号\] \- \[ティルデ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: CTRL+SHIFT+\`

## プラグイン コマンド ID

```
EEID_INSERT_TILDE (4306)

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4306);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4306
```