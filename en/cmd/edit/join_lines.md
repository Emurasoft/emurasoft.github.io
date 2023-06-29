# Join Lines command

### Summary

> Joins non-empty lines by replacing each newline with a space.

### Description

> Removes newline characters at wrap points in the selection. Similar to [**Remove Newline Characters** command](delete_cr_wrap), but this command inserts a space at each line at wrap points.

### How to Run

- Default Menu: **Convert** \> **Join Lines**
- [All Commands](../tools/all_commands): **Convert** \> **Join Lines**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_JOIN\_LINES (4378)

### Macros

#### \[JavaScript\]

> document.selection.Format(eeFormatJoinLines);

#### \[VBScript\]

> document.selection.Format eeFormatJoinLines