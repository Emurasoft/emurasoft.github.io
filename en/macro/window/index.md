# Window Object

## Properties

|     |     |
| --- | --- |
| **[Caption](caption)** | Returns the caption text for the window. |
| **[Children](children)** | Returns the Windows collection that represents child windows. |
| **[ClassName](class_name)** | Returns the class name for the window. |
| **[clipboardData](clipboarddata)** | Returns the clipboardData Object. |
| **[CombineHistory](combine_history)** | Specifies the undo/redo history to be combined or not combined. |
| **[DiscardUndo](discard_undo)** | Returns the flag to indicate whether EmEditor discards undo information to improve the speed of replace, insert or delete. |
| **[document](window_document)** | Returns the Document Object. |
| [**DroppedFiles**](droppedfiles) | Returns the DroppedFiles Object. |
| **[editor](window_editor)** | Returns the Editor Object. |
| **[Enabled](enabled)** | Returns whether the window is enabled for mouse and keyboard input. |
| [**ExStyle**](exstyle) | Returns the extended styles of the specified window. |
| **[Height](height)** | Returns or sets the height of the window. |
| **[hWnd](hwnd)** | Retrieves or sets the handle value of the window. |
| [**Interface**](interface) | Returns the Interface Object. |
| **[LeftX](leftx)** | Returns or sets the horizontal position of the specified window, in pixels. |
| **[OutputBar](output_bar)** | Returns the OutputBar Object. |
| **[Parent](parent)** | Returns the parent window object. |
| **[ProcessID](process_id)** | Returns the process identifier. |
| **[Redraw](window_redraw)** | Allows changes in EmEditor to be redrawn or prevents changes in EmEditor from being redrawn. |
| **[ScriptFullName](scriptfullname)** | Retrieves the complete path and file name of the currently running macro file. |
| **[ScriptName](scriptname)** | Retrieves only the file name of the currently running macro file. |
| [**Style**](style) | Returns the styles of the specified window. |
| **[scrollX](window_scrollx)** | Returns the horizontal position of the scroll bar. |
| **[scrollY](window_scrolly)** | Returns the vertical position of the scroll bar. |
| **[shell](shell)** | Returns the Shell Object. |
| **[status](window_status)** | Retrieves or sets a string displayed on the status bar. |
| **[ThreadID](thread_id)** | Returns the identifier of the thread that created the window. |
| **[Top](top)** | Returns or sets the vertical position of the specified window, in pixels. |
| **[Valid](valid)** | Returns whether the window handle is valid. |
| **[Visible](visible)** | Returns whether the window is visible. |
| **[WebBar](web_bar)** | Returns the WebBar Object. |
| **[Width](width)** | Returns or sets the width of the window. |

## Methods

|     |     |
| --- | --- |
| **[alert](window_alert)** | Displays a message in a simple dialog box with the OK button. |
| **[close](window_close)** | Closes the window. |
| **[confirm](window_confirm)** | Displays a message in a simple dialog box with the OK button and the <br> Cancel button. |
| **[CreatePopupMenu](createpopupmenu)** | Creates a popup menu. |
| **[FindWindow](find_window)** | Finds the child Window object by a class name and/or by a window title. |
| **[FindWindowByID](find_window_by_id)** | Finds the child window object by the window identifier. |
| **[print](window_print)** | Displays the Print dialog box. |
| **[prompt](window_prompt)** | Displays a dialog box to enter a string. |
| **[Quit](quit)** | Terminates the macro execution. |
| **[scrollBy](window_scrollby)** | Scrolls the window by the specified relative amount. |
| **[scrollTo](window_scrollto)** | Scrolls the window to the specified position. |
| **[SetFocus](set_focus)** | Sets the keyboard focus to the window. |
| **[SetForeground](set_foreground)** | Brings the window to foreground. |
| **[SetPosition](set_position)** | Sets the size and position of the window. |
| **[ShowTip](show_tip)** | Displays a tooltip. |
| **[Sleep](window_sleep)** | Pauses the macro execution for the specified time in milliseconds. |

## Version

Supported on EmEditor Professional Version 4.00 or later.


```{toctree}
:hidden:
:maxdepth: 1
caption
children
class_name
clipboarddata
combine_history
createpopupmenu
discard_undo
droppedfiles
enabled
exstyle
find_window
find_window_by_id
height
hwnd
interface
leftx
output_bar
parent
process_id
quit
scriptfullname
scriptname
set_focus
set_foreground
set_position
shell
show_tip
style
thread_id
top
valid
visible
web_bar
width
window_alert
window_close
window_confirm
window_document
window_editor
window_print
window_prompt
window_redraw
window_scrollby
window_scrollto
window_scrollx
window_scrolly
window_sleep
window_status
```
