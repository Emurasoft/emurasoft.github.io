# Logical Home command

### Summary

> Moves the cursor to the start of the current logical line.

### Description

> Moves the cursor to the start of the current logical line.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Logical Home**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: ALT+HOME

### Plug-in Command ID

- EEID\_LOGICAL\_HOME (4165)

### Macros

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineLogical);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineLogical
