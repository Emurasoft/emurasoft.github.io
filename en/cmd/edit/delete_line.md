# Delete Line(s) command

### Summary

> Deletes the selected lines or the current line.

### Description

> Deletes the selected lines or one logical line at the cursor.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Delete**
\> **Delete Line(s)**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+L

### Plug-in Command ID

- EEID\_DELETE\_LINE (4190)

### Macros

#### \[JavaScript\]

> document.selection.SelectLine();
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.SelectLine
>
> document.selection.Delete 1