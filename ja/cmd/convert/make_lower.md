# \[小文字に変換\] コマンド

## 概要

選択範囲を小文字に変換します。

## 説明

選択範囲に存在する大文字を小文字に変換します。例えば、A は a に、Ａ (全角) は ａ (全角) に、Ä は ä に、Λ は λ に変換されます。

## 実行方法

- 既定のメニュー: \[変換\] \- \[小文字に変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[小文字に変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+U

## プラグイン コマンド ID

```
EEID_MAKE_LOWER (4150)```

## マクロ

### \[JavaScript\]

```
document.selection.ChangeCase(eeCaseLowerCase);
```

### \[VBScript\]

```
document.selection.ChangeCase eeCaseLowerCase
```
