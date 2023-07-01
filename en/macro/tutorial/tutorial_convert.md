# Convert Character in Selection Range (Tutorial)

To convert characters in Selection Range, add the seventh line to our Tutorial macro:

#### \[JavaScript\]

> document.selection.Text = "EmEditor supports macros.";
>
> document.selection.NewLine();
>
> document.selection.Text = "\\tEmEditor is a text editor.";
>
> document.selection.CharLeft( false, 12 );
>
> document.selection.DeleteLeft( 15 );
>
> document.selection.CharRight( true, 9 );
>
> document.selection.ChangeCase( eeCaseUpperCase );

#### \[VBScript\]

> document.selection.Text = "EmEditor supports macros."
>
> document.selection.NewLine
>
> document.selection.Text = Chr(9) & "EmEditor is a text editor."
>
> document.selection.CharLeft False, 12
>
> document.selection.DeleteLeft 15
>
> document.selection.CharRight True, 9
>
> document.selection.ChangeCase eeCaseUpperCase

Save the above macro and run it in a new EmEditor window. Notice that the
characters of the selected text have converted to upper case:

TEXT EDITor.

**[ChangeCase Method](../selection/selection_changecase)** takes an
argument that specifies
whether characters are to be converted to upper case or lower case.

Similarly, the following methods are provided to convert characters in Selection Range.
For further details, such as explanations of arguments that methods take, refer to each
method.

|     |     |
| --- | --- |
| **[ChangeCase](../selection/selection_changecase)** | Convert characters to upper or lower case. |
| **[ChangeWidth](../selection/selection_changewidth)** | Convert characters to half-width or full-width characters. |
| **[Format](../selection/selection_format)** | Insert a newline character at a line wrap position of the selection range or delete a newline. |
| **[Indent](../selection/selection_indent)** | Indent the section specified by the selection range. |
| **[Tabify](../selection/selection_tabify)** | Convert spaces to tabs in the selection range. |
| **[UnIndent](../selection/selection_unindent)** | Unindent the section specified by the selection range. |
| **[Untabify](../selection/selection_untabify)** | Convert tabs to spaces in the selection range. |

## Next Topic:
