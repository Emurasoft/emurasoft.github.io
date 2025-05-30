# \[システム既定エンコードで読み直し\] コマンド

## 概要

[システム既定エンコード](../../glossary/systemdefaultencoding) で読み直します。

## 説明

このコマンドを実行すると、現在開かれているファイルを、ディスクから読み直し、そのときのエンコードは、 [システム既定エンコード](../../glossary/systemdefaultencoding) が使用されます。EmEditor
上で文書が変更されている場合、「変更を破棄して続行しますか?」という確認のメッセージ ボックスが表示されます。ここで、\[はい\]
を選択すると、現在の文書を保存せずに破棄し、新しい内容が読み込まれます。ここで \[いいえ\]
を選択すると、読み直しを中止し、現在の文書の編集を続けることができます。

## 実行方法

- 既定のメニュー: \[ファイル\] \- \[読み直し\] \- \[システム既定\]
- [すべてのコマンド](../../glossary/allcommands): \[ファイル\] \- \[システム既定\]
- ツール バー: ![](../../images/reload.png) (矢印の部分) \- \[システム既定\]
- ステータス バー: エンコードの項目をダブルクリック \- \[システム既定\]
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_FILE_RELOAD_ANSI (4110)
```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(4110);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4110
```
