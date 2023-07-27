# Move Cursor (Tutorial)

To move the cursor, add the fourth line to our tutorial macro as follows:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
Save the macro and run it in a new EmEditor window. Notice that the cursor is positioned
at 12 characters left from the end of the line, or at the position where the first 't' character of "text editor" is.
[CharLeft Method](../selection/selectioncharleft) moves
the cursor the specified number of characters to the left.
The first argument (false) of the[CharLeft \
Method](../selection/selectioncharleft) specifies whether the selection range is to be changed. That is,
it specifies whether you want to use the SHIFT key when you
use the LEFT ARROW key on your keyboard.
The following methods are provided to manipulate cursor movements.
|     |     |
| --- | --- |
|[CharLeft](../selection/selectioncharleft) | Move the cursor the specified number of characters to the left. Equivalent to the <br> LEFT ARROW key. |
|[CharRight](../selection/selectioncharright) | Move the cursor the specified number of characters to the right. Equivalent to the <br> RIGHT ARROW key. |
|[LineDown](../selection/selectionlinedown) | Move the cursor the specified number of lines down. Equivalent to the <br> DOWN ARROW key. |
|[LineUp](../selection/selectionlineup) | Move the cursor the specified number of lines up. Equivalent to the UP <br> ARROW key. |
|[WordLeft](../selection/selectionwordleft) | Move the cursor one word to the left. Equivalent to CTRL + LEFT ARROW. |
|[WordRight](../selection/selectionwordright) | Move the cursor one word to the right. Equivalent to CTRL + RIGHT ARROW. |
|[PageDown](../selection/selectionpagedown) | Move the cursor down one tab. Equivalent to the PAGE DOWN key. |
|[PageUp](../selection/selectionpageup) | Move the cursor up one page. Equivalent to the PAGE UP key. |
|[StartOfLine](../selection/selectionstartofline) | Move the cursor to the beginning of the line. Equivalent to the HOME key. |
|[EndOfLine](../selection/selectionendofline) | Move the cursor to the end of the line. Equivalent to the END key. |
|[StartOfDocument](../selection/selectionstartofdocument) | Move the cursor to the start of a document. Equivalent to CTRL+ HOME. |
|[EndOfDocument](../selection/selectionendofdocument) | Move the cursor to the end of a document. Equivalent to CTRL+ END. |
|[GoToBrace](../selection/selectiongotobrace) | Move the cursor to the matching brace. |
The following method moves the cursor to the specified line or digit position.
|     |     |
| --- | --- |
|[SetActivePoint](../selection/selectionsetactivepoint) | Set the cursor position. |
```

## Next Topic:
