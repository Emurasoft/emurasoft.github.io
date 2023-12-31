# \[ツールの一覧\] コマンド

## 概要

指定するツールを実行します (複数項目)。

## 説明

このコマンドは通常、複数のメニュー項目から成り立っています。 [\[外部ツール\] ダイアログ ボックス](../../dlg/tools/index) で定義されている外部ツールに対して実行できます。このコマンドを実行すると、指定した外部ツールを実行します。

## 実行方法

- 既定のメニュー: \[ツール\] \- \[外部ツール\] \- (ツール名)
- [すべてのコマンド](../../glossary/allcommands): \[外部ツール\] \- (ツール名)
- ツール バー: ツール ツール バーの各ボタン
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_TOOL1 から EEID_TOOL1 + 255 まで (8192 から 8192 + 255 まで)```

## マクロ

### \[JavaScript\]

```
editor.ExecuteCommandByID(8192+i);  // i は 0 から 255 までの整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 8192+i  ' i は 0 から 255 までの整数
```
