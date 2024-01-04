# \[次の文字列を検索\] コマンド

## 概要

次のカーソル位置の文字列を検索します。

## 説明

文字列が選択されている場合、その文字列を下方向に検索します。文字列が選択されていない場合、カーソル位置の単語を下方向に検索します。

## 実行方法

- 既定のメニュー: \[検索\] \- \[次の文字列を検索\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[次の文字列を検索\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Ctrl+F3

## プラグイン コマンド ID

```
EEID_FIND_NEXT_WORD (4204)```

## マクロ

### \[JavaScript\]

```
document.selection.FindRepeat(eeFindRepeatNext | eeFindRepeatWord);
```

### \[VBScript\]

```
document.selection.FindRepeat eeFindRepeatNext Or eeFindRepeatWord
```
