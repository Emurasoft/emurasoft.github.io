# \[単語の最初の文字を大文字に変換\] コマンド

## 概要

選択範囲の単語の最初の文字を大文字に変換します。

## 説明

選択範囲の単語の最初の文字を大文字に変換します。他の文字は小文字に変換されます。

## 実行方法

- 既定のメニュー: \[変換\] \- \[単語の最初の文字を大文字に変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[単語の最初の文字を大文字に変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_CAPITALIZE (4381)```

## マクロ

### \[JavaScript\]

```
document.selection.ChangeCase(eeCaseCapitalize);
```

### \[VBScript\]

```
document.selection.ChangeCase eeCaseCapitalize
```
