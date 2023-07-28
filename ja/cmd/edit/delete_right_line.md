# \[行右削除\] コマンド

## 概要

1 行のカーソルから右を削除します。

## 説明

論理行 1 行のカーソル位置から右側を行末まで削除します。

## 実行方法

- 既定のメニュー: \[編集\] \- \[高度な操作\] \- \[行右削除\]
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[行右削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+D

## プラグイン コマンド ID

```
EEID_DELETE_RIGHT_LINE (4191)```

## マクロ

### \[JavaScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.EndOfLine true,eeLineLogical
document.selection.Delete 1
```
