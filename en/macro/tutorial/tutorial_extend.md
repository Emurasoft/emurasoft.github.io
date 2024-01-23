# Change Selection Range (Tutorial)

To change Selection Range, add the sixth line to our tutorial macro:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
```
Save the above macro and run it in a new EmEditor Window. Notice that the "text edit" part is displayed highlighted
as follows:
text editor.
We passed true to the first parameter of theCharRight Method, which
has moved the cursor as well as changed the selection range; pressing the RIGHT
ARROW key while holding down
the SHIFT key gives you the same effect.
Similarly, most of the methods for cursor movements receive arguments to change the selection range
(See [Move Cursor](tutorial_move)).
More methods are available to change the selection range:
|     |     |
| --- | --- |
|[SelectAll](../selection/selection_selectall) | Selects the entire text. Equivalent to the CTRL + A key. |
|[SelectLine](../selection/selection_selectline) | Selects the line in which the cursor is located. |
|[SelectWord](../selection/selection_selectword) | Selects an entire word at the cursor. |
|[Collapse](../selection/selection_collapse) | Turns off the current option. Equivalent to the ESC key. |

You can setup or check the status of the selection range in the following properties:
|     |     |
| --- | --- |
|[IsActiveEndGreater](../selection/selection_isactiveendgreater) | Shows whether the active point matches the end part of the selection range. |
|[IsEmpty](../selection/selection_isempty) | Shows whether the selection range is empty. |
|[Mode](../selection/selection_mode) | Gets or setup the selection type(vertical selection, line selection etc.). |
