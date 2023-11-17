# \[日付と時刻\] コマンド

## 概要

現在の日付と時刻を挿入します。

## 説明

カーソル位置に現在の日付と時刻を挿入します。日付、空白、時刻の順に挿入します。時刻と日付のフォーマットは、コントロール パネルの
\[地域と言語のオプション\] の \[地域オプション\] ページの \[時刻\] と \[短い形式\] で設定できます。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[日付と時刻\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[日付と時刻\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Shift+F5

## プラグイン コマンド ID

```
EEID_INSERT_DATE_TIME (4138)```

## マクロ

### \[JavaScript\]

```
document.selection.InsertDate(eeDateDateTime);
```

### \[VBScript\]

```
document.selection.InsertDate eeDateDateTime
```
