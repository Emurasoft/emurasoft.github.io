# Toggle Toolbar command

### Summary

> Shows or hides a specified toolbar (multiple items).

### Description

> Shows or hides a specified toolbar (multiple items).

### How to Run

- Default Menu: **View** \> **Toolbars**
- [All Commands](../tools/all_commands): **View** >
**Toolbars**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- From EEID\_TOOLBAR1 through EEID\_TOOLBAR1 + 255 (from 22976 through 22976 + 255)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(22976 + i);  // i is an integer from 0 through 255

#### \[VBScript\]

> editor.ExecuteCommandByID 22976 + i  ' i is an integer from 0 through 255