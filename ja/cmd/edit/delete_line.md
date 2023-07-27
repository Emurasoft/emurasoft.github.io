# \[行削除\] コマンド

## 概要

選択行または現在行を削除します。

## 説明

選択行またはカーソルを含む論理行 1 行を削除します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[行削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+L

## プラグイン コマンド ID

```
EEID_DELETE_LINE (4190)```

## マクロ

### \[JavaScript\]

```
document.selection.SelectLine();
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.SelectLine
document.selection.Delete 1
```
