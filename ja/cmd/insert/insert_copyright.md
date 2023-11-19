# \[コピーライトを挿入\] コマンド

## 概要

コピーライトを挿入します。

## 説明

カーソル位置にコピーライト文字 © を挿入します。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[記号\] \- \[コピーライト\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[記号\] \- \[コピーライト\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+Ctrl+C

## プラグイン コマンド ID

```
EEID_INSERT_COPYRIGHT (4314)

## マクロ

### \[JavaScript\]

```
document.selection.Text="©";
```

### \[VBScript\]

```
document.selection.Text="©"
```