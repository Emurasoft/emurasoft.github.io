# \[文字コード値\] コマンド

## 概要

カーソル位置の文字コード値を表示します。

## 説明

このコマンドを実行すると、 [\[文字コード値\] ダイアログ ボックス](../../dlg/character_code_value_dialog/index) を表示して、カーソル位置にある文字の文字コード値を 16 進数で表示します。U+xxxx
という形式は、Unicode の文字コードを 4 または 5 桁の 16 進数で表しています。Unicode 以外のファイル形式の場合、ANSI ( [システム既定エンコード](../../glossary/systemdefaultencoding))
による文字コードも 2 桁の 16 進数で表示します。

## 実行方法

- 既定のメニュー: \[表示\] \- \[文字コード値\]
- [すべてのコマンド](../../glossary/allcommands): \[表示\] \- \[文字コード値\]
- ツール バー:
- ステータス バー: なし
- 既定のショートカット: Ctrl+I

## プラグイン コマンド ID

```
EEID_WATCH_CHAR_CODE (4213)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4213);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4213
```
