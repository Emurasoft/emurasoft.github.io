# \[行コピー\] コマンド

## 概要

選択行または現在行をクリップボードにコピーします。

## 説明

選択行またはカーソル位置の論理行 1 行をコピーして、その内容をクリップボードに保存します。この操作の後、別の場所にカーソルを移動して
[\[貼り付け\] コマンド](edit_paste) を実行することにより、コピーした 1
行のテキストを他の場所にコピーすることができます。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[コピー\] \- \[行コピー\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_EDIT_COPY_LINE (4192)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4192);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4192
```
