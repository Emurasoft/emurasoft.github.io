# Insert LF command

### Summary

> Inserts a line feed at the current cursor position.

### Description

> Inserts a line feed (LF) at the current cursor position. EmEditor can edit files with the
> mixture of CR and LF as newline characters. Pressing the ENTER key inserts the same
> newline character at the current line, CR only, LF only or CR+LF. This command
> always inserts LF only no matter what newline character is used at the current
> line.

### How to Run

- Default Menu: **Insert** \> **LF Only**
- [All Commands](../tools/all_commands): **Insert** \> **LF Only**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_INSERT\_LF (4146)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4146);

#### \[VBScript\]

> editor.ExecuteCommandByID 4146
