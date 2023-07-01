# Char Left Extend command

### Summary

> Extends the selection one character to the left.

### Description

> Extends the selection one character to the left. If the cursor is at the
> beginning of a line, this command moves the cursor to the end of the
> previous line.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Char Left Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+LEFT ARROW

### Plug-in Command ID

- EEID\_SHIFT\_LEFT (4173)

### Macros

#### \[JavaScript\]

> document.selection.CharLeft(true,1);

#### \[VBScript\]

> document.selection.CharLeft true,1
