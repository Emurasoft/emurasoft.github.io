# Documents List command

### Summary

> Switches to the specified document (multiple items).

### Description

> Switches to the specified EmEditor document. If the specified document is minimized, it will restore its
> normal size. This command consists of multiple menu items.

### How to Run

- Default Menu: **Window** \> ( **document name**)
- [All Commands](../tools/all_commands): **Window**
\> ( **document name**)
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- From EEID\_WINDOW\_MENU through EEID\_WINDOW\_MENU + 255 (from 5376 through 5376 + 255)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(5376 + i);  // i is an integer from 0
> through 255

#### \[VBScript\]

> editor.ExecuteCommandByID 5376 + i   ' i is an integer from 0
> through 255