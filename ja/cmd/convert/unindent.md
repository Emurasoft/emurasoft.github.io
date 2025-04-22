# \[逆インデント\] コマンド

## 概要

選択範囲の行インデントを少なくします。

## 説明

選択範囲の行の最初にタブ文字を挿入して行インデントを減らします。改行コードを含む複数行が選択されている場合の [\[タブの左移動/逆インデント\] コマンド](../edit/shift_tab) と同等です。

## 実行方法

- 既定のメニュー: \[変換\] \- \[逆インデント\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[逆インデント\]
- ツール バー: ![](../../images/unindent..png)
- ステータス バー: なし
- 既定のショートカット: Shift+Tab

## プラグイン コマンド ID

```
EEID_UNINDENT (4359)
```

## マクロ

### \[JavaScript\]

```
document.selection.UnIndent();
```

### \[VBScript\]

```
document.selection.UnIndent
```
