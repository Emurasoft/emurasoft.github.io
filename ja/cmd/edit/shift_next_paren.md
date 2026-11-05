# \[選択範囲を対応する括弧へ\] コマンド

## 概要

選択範囲を対応する括弧へ移動します。

## 説明

カーソル位置に括弧が存在する場合、選択範囲をそれに対応する括弧へ移動します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[選択範囲の変更\] \- \[選択範囲を対応する括弧へ\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+\]

## プラグイン コマンド ID

```
EEID_SHIFT_NEXT_PAREN (4277)```

## マクロ

### \[JavaScript\]

```
document.selection.GoToBrace(true);
```

### \[VBScript\]

```
document.selection.GoToBrace true
```
