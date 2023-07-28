# \[再変換\] コマンド

## 概要

再変換対応の IME を使って確定文字列の再変換を行います。

## 説明

再変換対応の IME (Microsoft IME 日本語入力システム、Justsystem 日本語入力システム ATOK など)
を使って選択範囲の確定文字列の再変換を行います。

## 実行方法

- 既定のメニュー: \[変換\] \- \[再変換\]
- [すべてのコマンド](../../glossary/allcommands): \[変換\] \- \[再変換\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし (通常、IME 側の設定により、日本語キーボードの \[変換\] キーで再変換できます)

## プラグイン コマンド ID

```
EEID_RECONVERT (4199)```

## マクロ

## \[JavaScript\]

```
editor.ExecuteCommandByID(4199);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4199
```
