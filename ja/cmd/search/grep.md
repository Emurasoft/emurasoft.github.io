# \[ファイルから検索\] コマンド

## 概要

複数のファイルから検索します。

## 説明

複数のファイルから検索します。このコマンドを実行すると、 [\[ファイルから検索\] ダイアログ ボックス](../../dlg/find_in_files/index) が表示されます。ここで、検索する文字列、ファイルの種類、検索するフォルダ、各種オプションを指定して、ファイルから検索することができます。ファイルから検索の結果は、文字列が見つかったファイルのフル
パスと行番号の一覧となって EmEditor のウィンドウ上で表示されます。そこで [\[タグ ジャンプ\] コマンド](../edit/tag_jump) を実行することにより、見つかった文字列に素早くジャンプすることができます。

## 実行方法

- 既定のメニュー: \[検索\] \- \[ファイルから検索\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[ファイルから検索\]
- ツール バー: ![](../../images/grep.png)
- ステータス バー: なし
- 既定のショートカット: Ctrl+Shift+F

## プラグイン コマンド ID

```
EEID_GREP (4207)
```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4207);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4207
```
