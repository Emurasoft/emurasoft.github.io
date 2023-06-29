# Delete Characters

To delete characters, add the fifth line to our tutorial macro:

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

Save the above macro and run it in a new EmEditor window. Notice that the 15 characters from
the left side
of the text editor (that is, "(tab)EmEditor is a ") are deleted. The text should now read as follows:

"EmEditor supports macros _."_

"text editor."

**DeleteLeft** **Method** deletes the specified number of characters from the left side of a string.
If text is being selected, the selected text is deleted; pressing the Backspacekey on your keyboard gives you
the same effect.

Similarly, the following methods are provided to delete characters:

|     |     |
| --- | --- |
| **[Delete](../selection/selection_delete)** | Delete the selected text. If no text is selected, it deletes the specified number of characters from the right side<br> of a string. Equivalent to the Delete key. |
| [**DeleteLeft**](../selection/selection_deleteleft) | Delete the selected text. If no text is selected, <br> it deletes the specified number of characters from the left side of a string. Equivalent to the Backspace key. |

You can delete words or lines by combining methods:

#### \[JavaScript\]

|     |     |
| --- | --- |
| Delete a word. | document.selection.SelectWord();<br> document.selection.Delete(); |
| Delete a word left of the cursor. | document.selection.WordLeft(true);<br> document.selection.Delete(); |
| Delete a word right of the cursor. | document.selection.WordRight(true);<br> document.selection.Delete(); |
| Delete a line. | document.selection.SelectLine();<br> document.selection.Delete(); |
| Delete a line left. | document.selection.StartOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| Delete a line right. | document.selection.EndOfLine(true, eeLineLogical);<br> document.selection.Delete(); |
| Delete an entire document. | document.selection.SelectAll();<br> document.selection.Delete(); |

#### \[VBScript\]

|     |     |
| --- | --- |
| Delete a word. | document.selection.SelectWord<br> document.selection.Delete |
| Delete a word left of the cursor. | document.selection.WordLeft True<br> document.selection.Delete |
| Delete a word right of the cursor. | document.selection.WordRight True<br> document.selection.Delete |
| Delete a line. | document.selection.SelectLine<br> document.selection.Delete |
| Delete a line left. | document.selection.StartOfLine True, eeLineLogical<br> document.selection.Delete |
| Delete a line right. | document.selection.EndOfLine True, eeLineLogical<br> document.selection.Delete |
| Delete an entire document. | document.selection.SelectAll<br> document.selection.Delete |

## Next Topic: