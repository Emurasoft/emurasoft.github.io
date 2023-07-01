# Text プロパティ ()

選択されたテキストを取得、またはテキストを挿入します。

#### \[JavaScript\]

_str_ = document.selection. **Text**;

document.selection. **Text** = _str_;

#### \[VBScript\]

_str_ = document.selection. **Text**

document.selection. **Text** = _str_

## 例

#### \[JavaScript\]

str = document.selection.Text;

alert( "選択されていたテキストは " + str );

document.selection.Text = "こんにちは";

#### \[VBScript\]

str = document.selection.Text

alert "選択されていたテキストは " & str

document.selection.Text = "こんにちは"

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
