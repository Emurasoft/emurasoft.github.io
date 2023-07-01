# Text 属性 (Selection ����)

检索被选取的文本，或在光标位置处插入一个字符串。

#### \[JavaScript\]

_str_ = document.selection. **Text**;

document.selection. **Text** = _str_;

#### \[VBScript\]

_str_ = document.selection. **Text**

document.selection. **Text** = _str_

## 示例

#### \[JavaScript\]

str = document.selection.Text;

alert( "The selected text is " + str );

document.selection.Text = "Hello";

#### \[VBScript\]

str = document.selection.Text

alert "The selected text is " & str

document.selection.Text = "Hello"

## 版本

支持 EmEditor 4.00 或之后的版本。
