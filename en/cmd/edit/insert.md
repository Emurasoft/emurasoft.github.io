# Insert/Overwrite command

### Summary

> Toggles insert/overwrite mode.

### Description

> Toggles insert/overwrite mode. EmEditor usually starts with the insert mode. When EmEditor is in insert mode, the cursor is a vertical bar, and inserting a character will not delete any existing characters. When EmEditor is in overwrite mode, the cursor becomes a solid rectangle, and inserting a character will overwrite existing characters at the cursor position.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Insert** \> **Toggle Insert/Overwrite**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: Insert

### Plug-in Command ID

- EEID\_INSERT (4142)

### Macros

#### \[JavaScript\]

> document.selection.OverwriteMode = !document.selection.OverwriteMode;

#### \[VBScript\]

> document.selection.OverwriteMode = NOT document.selection.OverwriteMode
