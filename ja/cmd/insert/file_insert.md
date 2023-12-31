# \[挿入\] コマンド

## 概要

カーソル位置にファイルを挿入します。

## 説明

このコマンドを実行すると、\[挿入\] ダイアログ
ボックスが表示され、挿入したいファイルを選択することができます。ファイルを選択すると、そのファイルを読み込んで、カーソル位置にファイルの中身を挿入します。

\[挿入\] ダイアログ ボックス内で、各チェック ボックスや選択項目についてのヘルプを表示するには、ダイアログ ボックスの右上の \[?\]
マークをクリックしてから、調べたい項目をクリックします。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[挿入\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[挿入\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_FILE_INSERT (4108)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4108);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4108
```
