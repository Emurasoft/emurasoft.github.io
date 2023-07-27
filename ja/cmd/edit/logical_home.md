# \[論理行の行頭へ\] コマンド

## 概要

論理行の行頭へ移動します。

## 説明

カーソル位置を論理行の行頭へ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[論理行の行頭へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+Home

## プラグイン コマンド ID

```
EEID_LOGICAL_HOME (4165)```

## マクロ

## \[JavaScript\]

```
document.selection.StartOfLine(false,eeLineLogical);
```

## \[VBScript\]

```
document.selection.StartOfLine false,eeLineLogical
```
