# \[最近のやり直し (複数項目)\] コマンド

## 概要

指定する動作までやり直します。

## 説明

指定する動作までやり直します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[やり直し\] \- \[最近のやり直し (複数項目)\]
- ツール バー: ![](../../images/editredo.gif) (矢印の部分)
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_REDO_RECENT から EEID_REDO_RECENT + 63 まで (22912 から 22912 + 63 まで)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(22912 + i);  // i は 0 から 63 までの整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22912  ' i は 0 から 63 までの整数
```
