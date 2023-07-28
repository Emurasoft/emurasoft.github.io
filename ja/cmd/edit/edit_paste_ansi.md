# \[システム既定エンコードで貼り付け\] コマンド

## 概要

システム既定エンコードで貼り付けます。

## 説明

カーソル位置にクリップボード内のテキストを [システム既定エンコード](../../glossary/systemdefaultencoding) で貼り付けます。通常、この操作の前に
[**\[コピー\]** コマンド](edit_copy)、または [**\[切り取り\]** コマンド](edit_cut) によってテキストをクリップボードに保存しておきます。プロパティの [**\[基本\]** タブ](../../dlg/properties/general/index) で、 **\[常にANSIで貼り付け\]**
チェック ボックスがチェックされている場合は、 [**\[貼り付け\]** コマンド](edit_paste) と同じ動作になります。

## 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[貼り付け\] \- \[システム既定エンコードで貼り付け\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+Ctrl+V

## プラグイン コマンド ID

```
EEID_EDIT_PASTE_ANSI (4262)```

## マクロ

### \[JavaScript\]

```
document.selection.Paste(eeCopySystemDefault);
```

### \[VBScript\]

```
document.selection.Paste eeCopySystemDefault
```
