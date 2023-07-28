# \[CR+LFを挿入\] コマンド

## 概要

カーソル位置に CR と LF を挿入します。

## 説明

カーソル位置に CR (復帰) と LF (改行) を挿入します。EmEditor では、CR と LF の混じった文書が編集できます。Enter
を入力すると、その行で使用されている改行コードと同じ改行コードを CR、LF、または CR+LF
のいずれかから自動的に選択されて挿入されます。このコマンドを実行すると、その行で使用されている改行コードによらずに、常に CR+LF を挿入します。

## 実行方法

- 既定のメニュー: \[挿入\] \- \[CR+LF\]
- [すべてのコマンド](../../glossary/allcommands): \[挿入\] \- \[CR+LF\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

## プラグイン コマンド ID

```
EEID_INSERT_CR_LF (4274)```

## マクロ

## \[JavaScript\]

```
editor.ExecuteCommandByID(4274);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4274
```
