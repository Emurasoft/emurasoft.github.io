# Previous Bookmark in This Group command

### Summary

> Goes to the previous bookmark in this group.

### Description

> Moves the cursor to the previous bookmark in this group. If no bookmark exists on
> the current document, this command will go to the last bookmark in the
> previous document. If only one document contains bookmarks, it will go
> straight to the last bookmark of that document.

### How to Run

- Default Menu: **Bookmarks** \> **This Group** \> **Previous Bookmark**
- [All Commands](../tools/all_commands): **Bookmarks** \> **This Group** \> **Previous Bookmark**
- Toolbar: ![](../../images/bookmarkprev.gif)
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+F2

### Plug-in Command ID

- EEID\_BOOKMARK\_PREV (4322)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4322);

#### \[VBScript\]

> editor.ExecuteCommandByID 4322
