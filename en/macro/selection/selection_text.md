# Text Property

Retrieves the selected text, or inserts a string at the cursor position.

#### \[JavaScript\]

_str_ = document.selection. **Text**;

document.selection. **Text** = _str_;

#### \[VBScript\]

_str_ = document.selection. **Text**

document.selection. **Text** = _str_

## Examples

#### \[JavaScript\]

str = document.selection.Text;

alert( "The selected text is " + str );

document.selection.Text = "Hello";

#### \[VBScript\]

str = document.selection.Text

alert "The selected text is " & str

document.selection.Text = "Hello"

## Version

Supported on EmEditor Professional Version 4.00 or later.