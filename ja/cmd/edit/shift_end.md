# \[選択範囲を行末へ\] コマンド

## 概要

選択範囲を行末へ移動します。

## 説明

選択範囲を表示行の行末へ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を行末へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Shift+End

## プラグイン コマンド ID

```
EEID_SHIFT_END (4182)```

## マクロ

### \[JavaScript\]

```
document.selection.EndOfLine(true,eeLineView);
```

### \[VBScript\]

```
document.selection.EndOfLine(true,eeLineView);
```
