# \[Unicode文字の強調を解除\] コマンド

### 概要

> 保存用エンコードに変換できないUnicode文字の強調表示を解除します。

### 説明

> 保存用エンコードに変換できないUnicode文字の強調表示を解除します。また、 [\[次のUnicode文字を検索\] \
> コマンド](find_next_unicode)、 [\[前のUnicode文字を検索\] コマンド](find_prev_unicode) で検索に使用する保存用エンコードをリセットします。

### 実行方法

- 既定のメニュー: \[検索\] \- \[Unicode文字の強調を解除\]
- [すべてのコマンド](../../glossary/allcommands): \[検索\] \- \[Unicode\] - \[Unicode文字の強調を解除\]
- ツール バー: なし
- ステータス バー: なし
- 既定のショートカット: Alt+F9

### プラグイン コマンド ID

- EEID\_ERASE\_UNICODE\_HILITE (4377)

### マクロ

#### \[JavaScript\]

> editor.ExecuteCommandByID(4377);

#### \[VBScript\]

> editor.ExecuteCommandByID 4377
