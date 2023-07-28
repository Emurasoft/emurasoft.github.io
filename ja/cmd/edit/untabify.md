# \[選択範囲のタブを空白に変換\] コマンド

## 概要

選択範囲のタブを空白に変換します。

## 説明

選択範囲に存在するタブ文字を空白に変換します。タブの桁数については、プロパティの
[**\[基本\]** タブ](../../dlg/properties/general/index) の

**\[タブ/インデント\]** ボタンをクリックし、 [**\[タブ/インデント\]** \
ダイアログ ボックス](../../dlg/properties/general/indent/index) で設定できます。

## 実行方法

- 既定のメニュー: \[変換\] \- \[Tabを空白に変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[Tabを空白に変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_UNTABIFY (4357)```

## マクロ

## \[JavaScript\]

```
document.selection.Untabify();
```

## \[VBScript\]

```
document.selection.Untabify
```
