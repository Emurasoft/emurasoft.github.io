# \[ワークスペースを名前を付けて保存\] コマンド

## 概要

ワークスペースを名前を付けて保存します。

## 説明

このコマンドを実行すると、Windows デスクトップ上の EmEditor ウィンドウの位置と開いているファイルのフル
パス名、カーソル位置などをワークスペース ファイルに名前を付けて保存します。次回 [\[ワークスペースを開く\] コマンド](workspace_open) を実行すると、このコマンドで保存した時の状態に復元します。

## 実行方法

- 既定のメニュー: \[ファイル\] \- \[ワークスペース\] \- \[ワークスペースを名前を付けて保存\]
- [すべてのコマンド](../../glossary/allcommands): \[ファイル\] \- \[ワークスペース\] \- \[ワークスペースを名前を付けて保存\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_WORKSPACE_SAVE_AS (3925)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(3925);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3925
```
