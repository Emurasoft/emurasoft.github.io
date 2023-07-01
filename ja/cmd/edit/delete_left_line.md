# \[行左削除\] コマンド

### 概要

> 1 行のカーソルから左を削除します。

### 説明

> 論理行 1 行のカーソル位置から左側を行頭まで削除します。

### 実行方法

- 既定のメニュー: なし
- [すべてのコマンド](../../glossary/allcommands): \[編集\] \- \[削除\] \- \[行左削除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: なし

### プラグイン コマンド ID

- EEID\_DELETE\_LEFT\_LINE (4302)

### マクロ

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineLogical);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineLogical
>
> document.selection.Delete 1
