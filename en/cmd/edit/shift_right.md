# Char Right Extend command

### Summary

> Extends the selection one character to the right.

### Description

> Extends the selection one character to the right. If the cursor is at the end
> of a line, this command moves the selection to the start of the next line.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Char Right Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+RIGHT ARROW

### Plug-in Command ID

- EEID\_SHIFT\_RIGHT (4172)

### Macros

#### \[JavaScript\]

> document.selection.CharRight(true,1);

#### \[VBScript\]

> document.selection.CharRight true,1
