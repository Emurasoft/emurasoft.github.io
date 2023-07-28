# \[選択範囲を1文字左へ\] コマンド

## 概要

選択範囲を 1 文字左へ移動します。

## 説明

選択範囲を 1 文字左へ移動します。カーソル位置が行末の場合、次の行の先頭に移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を1文字左へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Shift+Left

## プラグイン コマンド ID

```
EEID_SHIFT_LEFT (4173)```

## マクロ

## \[JavaScript\]

```
document.selection.CharLeft(true,1);
```

## \[VBScript\]

```
document.selection.CharLeft true,1
```
