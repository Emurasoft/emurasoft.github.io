# \[最近を元に戻す (複数項目)\] コマンド

## 概要

指定する動作まで元に戻します。

## 説明

指定する動作まで元に戻します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[元に戻す\] \- \[最近を元に戻す (複数項目)\]
- ツール バー: ![](../../images/editundo.gif) (矢印の部分)
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_UNDO_RECENT から EEID_UNDO_RECENT + 63 まで (22848 から 22848 + 63 まで)```

## マクロ

## \[JavaScript\]

```
editor.ExecuteCommandByID(22848 + i);  // i は 0 から 63 までの整数
```

## \[VBScript\]

```
editor.ExecuteCommandByID 22848  ' i は 0 から 63 までの整数
```
