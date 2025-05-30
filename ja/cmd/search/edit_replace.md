# \[置換\] コマンド

## 概要

指定した文字列を他の文字列で置換します。

## 説明

指定した文字列を他の文字列で置換します。このコマンドを実行すると、 [\[置換\] ダイアログ ボックス](../../dlg/replace/index) が表示されます。ここで、検索文字列、置換後の文字列や各種オプションを設定して、置換を開始することができます。

## 実行方法

- 既定のメニュー: \[検索\] \- \[置換\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[置換\]
- ツール バー: ![](../../images/replace.png)
- ステータス バー: なし
- 既定のショートカット: Ctrl+H

## プラグイン コマンド ID

```
EEID_EDIT_REPLACE (4201)
```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4201);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4201
```
