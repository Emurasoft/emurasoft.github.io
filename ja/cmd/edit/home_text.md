# \[行頭またはテキスト開始へ\] コマンド

## 概要

行頭またはテキスト開始位置へ移動します。

## 説明

カーソル位置を表示行の行頭へ移動します。ただし、行頭に空白が存在する場合で、現在のカーソル位置が空白を除いたテキストの開始位置でない場合、その空白を除いたテキストの開始位置に移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[行頭またはテキスト開始へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Home

## プラグイン コマンド ID

```
EEID_HOME_TEXT (4296)```

## マクロ

### \[JavaScript\]

```
document.selection.StartOfLine(false,eeLineView \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine false,eeLineView \| eeLineHomeText
```
