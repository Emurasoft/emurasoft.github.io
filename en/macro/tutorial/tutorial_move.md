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
```
Save the macro and run it in a new EmEditor window. Notice that the cursor is positioned
at 12 characters left from the end of the line, or at the position where the first 't' character of "text editor" is.
[CharLeft Method](../selection/selection_charleft) moves
the cursor the specified number of characters to the left.
The first argument (false) of the[CharLeft \
Method](../selection/selection_charleft) specifies whether the selection range is to be changed. That is,
it specifies whether you want to use the SHIFT key when you
use the LEFT ARROW key on your keyboard.
The following methods are provided to manipulate cursor movements.
|     |     |
| --- | --- |
|[CharLeft](../selection/selection_charleft) | Move the cursor the specified number of characters to the left. Equivalent to the <br> LEFT ARROW key. |
|[CharRight](../selection/selection_charright) | Move the cursor the specified number of characters to the right. Equivalent to the <br> RIGHT ARROW key. |
|[LineDown](../selection/selection_linedown) | Move the cursor the specified number of lines down. Equivalent to the <br> DOWN ARROW key. |
|[LineUp](../selection/selection_lineup) | Move the cursor the specified number of lines up. Equivalent to the UP <br> ARROW key. |
|[WordLeft](../selection/selection_wordleft) | Move the cursor one word to the left. Equivalent to CTRL + LEFT ARROW. |
|[WordRight](../selection/selection_wordright) | Move the cursor one word to the right. Equivalent to CTRL + RIGHT ARROW. |
|[PageDown](../selection/selection_pagedown) | Move the cursor down one tab. Equivalent to the PAGE DOWN key. |
|[PageUp](../selection/selection_pageup) | Move the cursor up one page. Equivalent to the PAGE UP key. |
|[StartOfLine](../selection/selection_startofline) | Move the cursor to the beginning of the line. Equivalent to the HOME key. |
|[EndOfLine](../selection/selection_endofline) | Move the cursor to the end of the line. Equivalent to the END key. |
|[StartOfDocument](../selection/selection_startofdocument) | Move the cursor to the start of a document. Equivalent to CTRL+ HOME. |
|[EndOfDocument](../selection/selection_endofdocument) | Move the cursor to the end of a document. Equivalent to CTRL+ END. |
|[GoToBrace](../selection/selection_gotobrace) | Move the cursor to the matching brace. |

The following method moves the cursor to the specified line or digit position.
|     |     |
| --- | --- |
|[SetActivePoint](../selection/selection_setactivepoint) | Set the cursor position. |
