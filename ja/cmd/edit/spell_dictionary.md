# \[辞書\] コマンド

## 概要

スペル チェックにこの辞書を選択します (複数項目)。

## 説明

スペル チェックにこの辞書を選択します。

## 実行方法

- 既定のメニュー: \[編集\] \- \[スペル チェック\] \- \[辞書\] \- (辞書)
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[スペル チェック\] \- \[辞書\] \- (辞書)
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_SELECT_DICTIONARY から EEID_SELECT_DICTIONARY + 255 まで (22016 から 22016 + 255 まで)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(22016 + i);  // i は 0 から 255 までの整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22016    ' i は 0 から 255 までの整数
```
