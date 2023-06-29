# Tab Left or Decrease Line Indent command

### Summary

> Moves the cursor one tab character to the left, or decreases the line
> indent.

### Description

> Moves the cursor one tab character to the left. If
> multiple lines are selected, this commands decreases the line indent by removing
> one tab character or the equivalent number of spaces at the start of each
> selected line.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Reverse Tab/Decrease Line**
**Indent**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_SHIFT\_TAB (4189)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4189);

#### \[VBScript\]

> editor.ExecuteCommandByID 4189