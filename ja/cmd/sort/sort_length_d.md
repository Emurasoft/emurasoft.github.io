# \[長い文字列から短い文字列へ並べ替え\] コマンド

## 概要

現在の列の文字列を長さで降順で並べ替えます。

## 説明

現在の列の文字列を長さで降順で並べ替えます。\[カスタマイズ\] ダイアログ ボックスの \[並べ替え\] ページの \[長さで並べ替える時、全角文字を2文字として扱う\] チェック ボックスにより、全角文字の数え方を指定することができます。

## 実行方法

- 既定のメニュー: \[並べ替え\] \- \[長い文字列から短い文字列へ並べ替え\]
- [すべてのコマンド](../../glossary/allcommands): \[並べ替え\] \- \[長い文字列から短い文字列へ並べ替え\]
- ツール バー: ![](../../images/sort_length_d.png)
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_SORT_LENGTH_A (3918)

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(3918);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3918
```