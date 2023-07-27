# Convert Character in Selection Range (Tutorial)

To convert characters in Selection Range, add the seventh line to our Tutorial macro:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
document.selection.ChangeCase( eeCaseUpperCase );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseUpperCase
Save the above macro and run it in a new EmEditor window. Notice that the
characters of the selected text have converted to upper case:
TEXT EDITor.
[ChangeCase Method](../selection/selectionchangecase) takes an
argument that specifies
whether characters are to be converted to upper case or lower case.
Similarly, the following methods are provided to convert characters in Selection Range.
For further details, such as explanations of arguments that methods take, refer to each
method.
|     |     |
| --- | --- |
|[ChangeCase](../selection/selectionchangecase) | Convert characters to upper or lower case. |
|[ChangeWidth](../selection/selectionchangewidth) | Convert characters to half-width or full-width characters. |
|[Format](../selection/selectionformat) | Insert a newline character at a line wrap position of the selection range or delete a newline. |
|[Indent](../selection/selectionindent) | Indent the section specified by the selection range. |
|[Tabify](../selection/selectiontabify) | Convert spaces to tabs in the selection range. |
|[UnIndent](../selection/selectionunindent) | Unindent the section specified by the selection range. |
|[Untabify](../selection/selectionuntabify) | Convert tabs to spaces in the selection range. |
```

## Next Topic:
