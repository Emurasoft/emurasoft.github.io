# Insert Characters (Tutorial)

To insert characters using a macro, use the **[Text Property](../selection/selection_text)**.
Modify our tutorial file as follows:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
The[NewLine Method](../selection/selectionnewline) added in the second line
inserts a newline character at the cursor position.
The code in the third line inserts a tab character at the beginning of the string.
A tab character is represented by "\\t" in JavaScript, and Chr(9) in VBScript.
You can also use the VBScript constant, vbTab, for a tab character.
The following tables list commonly used escape sequences in both scripting
languages.
```

### \[JavaScript\]

```
|     |     |     |
| --- | --- | --- |
| \\b | \\u0008 | Backspace. |
| \\t | \\u0009 | Horizontal Tab. |
| \\n | \\u000a | Newline character. |
| \\f | \\u000c | Form feed. |
| \\r | \\u000d | Carriage return. |
| \\" | \\u0022 | Double quote. |
| \\' | \\u0027 | Single quote. |
| \\\ | \\u005c | Backslash. |
| \\xXX |  | The Latin-1 character with the encoding specified by the two hexadecimal digits. |
| \\uXXXX |  | The Unicode character with the encoding specified by the four hexadecimal digits. |
```

### ![](../../images/g.gif) Reference:  [JScript \ Special Characters (Microsoft MSDN Library)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar\#String_literals)

### \[VBScript\]

```
|     |     |     |
| --- | --- | --- |
| vbCr | Chr(13) | Carriage return. |
| vbCrLf | Chr(13) & Chr(10) | Carriage return + newline character combination. |
| vbFormFeed | Chr(12) | Form feed. |
| vbLf | Chr(10) | Newline character. |
| vbNewLine | Chr(13) & Chr(10) or Chr(10) | Platform-specific newline character. Equivalent to vbCrLf in Windows. |
| vbTab | Chr(9) | Horizontal tab. |
| vbVerticalTab | Chr(11) | Vertical tab. |
```

### ![](../../images/g.gif) Reference:  [VBScript \ String Constants (Microsoft MSDN Library)](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/hh277t8e(v=vs.84))

## Tips

Line-endings are terminated with a combination of a \\r (CR) and a \\n (LF). Use the CR and LF in distinct manners.
For example, if you write:

document.selection.Text = "\\n";

only carriage return (LF) is inserted,
which is not a line-ending convention in Windows.
When you press the RETURN key in EmEditor, EmEditor inserts whatever line-ending (CR only, LF only, or CR+LF)
is used in that line.
If you want the same behavior upon pressing the RETURN key, as in
EmEditor, we recommend that you use the **[NewLine Method](../selection/selection_newline)**
or the **[writeln Method](../document/document_writeln)**.

## Next Topic:
