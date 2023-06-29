# Line Down Extend command

### Summary

> Extends the selection down one line.

### Description

> Extends the selection down one line. If no text is selected, this command will select the line directly below the cursor.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Line Down Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+DOWN ARROW

### Plug-in Command ID

- EEID\_SHIFT\_DOWN (4177)

### Macros

#### \[JavaScript\]

> document.selection.LineDown(true,1);

#### \[VBScript\]

> document.selection.LineDown true,1