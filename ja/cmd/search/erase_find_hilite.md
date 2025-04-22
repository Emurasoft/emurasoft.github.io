# \[検索文字列の強調を解除\] コマンド

## 概要

検索した文字列の強調表示を解除します。

## 説明

検索した文字列の強調表示を解除します。通常、検索を行うと、文書中の検索した文字列が強調表示されます。このコマンドを実行すると、その強調表示を解除します。

## 実行方法

- 既定のメニュー: \[検索\] \- \[検索文字列の強調を解除\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[検索文字列の強調を解除\]
- ツール バー:
![](../../images/erasefindhilite..png)
- ステータス バー: なし
- 既定のショートカット: Alt+F3

## プラグイン コマンド ID

```
EEID_ERASE_FIND_HILITE (4206)
```

## マクロ

### \[JavaScript\]

```
document.HighlightFind=false;
```

### \[VBScript\]

```
document.HighlightFind=false
```
