# \[対応するかっこへ\] コマンド

## 概要

対応するかっこへ移動します。

## 説明

カーソル位置にかっこが存在する場合、それに対応するかっこへ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[対応するかっこ\]
- ツール バー: ![](../../images/nextparen.gif)
- ステータス バー: なし
- 既定のショートカット: Ctrl+\]

## プラグイン コマンド ID

```
EEID_NEXT_PAREN (4276)```

## マクロ

### \[JavaScript\]

```
document.selection.GoToBrace(false);
```

### \[VBScript\]

```
document.selection.GoToBrace false
```
