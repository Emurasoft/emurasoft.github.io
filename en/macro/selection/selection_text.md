# Text Property (Selection Object)

Retrieves the selected text, or inserts a string at the cursor position. If the text is too long when retrieving the text, the property fails. The maximum supported length, in UTF-16 characters, is 0x19fffffe when using V8; otherwise, it is 0x3ffffffe.

## 

### \[JavaScript\]

```
str = document.selection.Text;
document.selection.Text = str;
```

### \[VBScript\]

```
str = document.selection.Text
document.selection.Text = str
```

## Examples

### \[JavaScript\]

```
str = document.selection.Text;
alert( "The selected text is " + str );
document.selection.Text = "Hello";
```

### \[VBScript\]

```
str = document.selection.Text
alert "The selected text is " & str
document.selection.Text = "Hello"
```

## Version

Supported on EmEditor Professional Version 4.00 or later.
