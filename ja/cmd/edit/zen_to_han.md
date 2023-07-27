# \[半角に変換\] コマンド

## 概要

選択範囲を半角に変換します。

## 説明

選択範囲に存在する全角文字を半角文字に変換します。例えば、Ａ (全角) は A (半角) に、ア (全角) は ｱ （半角) に変換します。

## 実行方法

- 既定のメニュー: \[変換\] \- \[半角に変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[半角に変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_ZEN_TO_HAN (4151)```

## マクロ

### \[JavaScript\]

```
document.selection.ChangeWidth(eeWidthHalfWidth \| eeWidthAllTypes);
```

### \[VBScript\]

```
document.selection.ChangeWidth eeWidthHalfWidth Or eeWidthAllTypes
```
