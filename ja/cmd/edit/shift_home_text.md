# \[選択範囲を行頭またはテキスト開始へ\] コマンド

## 概要

選択範囲を行頭またはテキスト開始位置へ移動します。

## 説明

選択範囲を表示行の行頭へ移動します。ただし、行頭に空白が存在する場合で、現在のカーソル位置が空白を除いたテキストの開始位置でない場合、その空白を除いたテキストの開始位置に移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を行頭またはテキスト開始へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+Ctrl+Shift+Home

## プラグイン コマンド ID

```
EEID_SHIFT_HOME_TEXT (4297)```

## マクロ

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineView \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineView Or eeLineHomeText
```
