# \[スペル チェックの提案\] コマンド

## 概要

正しいスペル チェック用にこの提案を選択します (複数項目)。

## 説明

正しいスペル チェック用にこの提案を選択します。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[スペル チェック\] \- (スペル チェックの提案)
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_SPELL_SUGGEST から EEID_SPELL_SUGGEST + 31 まで (8768 から 8768 + 31 まで)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(8768 + i);  // i は 0 から 31 までの整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 8768    ' i は 0 から 31 までの整数
```
