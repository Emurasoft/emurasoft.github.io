# \[対応する括弧へ\] コマンド

## 概要

対応する括弧へ移動します。

## 説明

カーソル位置に括弧が存在する場合、それに対応する括弧へ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[水平にカーソル移動\] \- \[対応する括弧\]
- ツール バー: ![](../../images/nextparen.png)
- ステータス バー: なし
- 既定のショートカット: Ctrl+\]

## プラグイン コマンド ID

```
EEID_NEXT_PAREN (4276)
```

## マクロ

### \[JavaScript\]

```
document.selection.GoToBrace(false);
```

### \[VBScript\]

```
document.selection.GoToBrace false
```
