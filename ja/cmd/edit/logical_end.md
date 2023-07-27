# \[論理行の行末へ\] コマンド

## 概要

論理行の行末へ移動します。

## 説明

カーソル位置を論理行の行末へ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[論理行の行末へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+End

## プラグイン コマンド ID

```
EEID_LOGICAL_END (4167)```

## マクロ

### \[JavaScript\]

```
document.selection.EndOfLine(false,eeLineLogical);
```

### \[VBScript\]

```
document.selection.EndOfLine false,eeLineLogical
```
