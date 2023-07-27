# \[単語選択を開始\] コマンド

## 概要

カーソル位置の単語を選択します。

## 説明

カーソル位置の単語を選択します。単語の右側に空白があっても、その空白は選択されません。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[単語を選択\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+F8

## プラグイン コマンド ID

```
EEID_SELECT_WORD (4251)```

## マクロ

### \[JavaScript\]

```
document.selection.SelectWord();
```

### \[VBScript\]

```
document.selection.SelectWord
```
