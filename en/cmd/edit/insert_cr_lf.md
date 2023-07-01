# Insert CR and LF command

### Summary

> Inserts a carriage return and a line feed at the current cursor position.

### Description

> Inserts a carriage return (CR) and a line feed (LF) at the current cursor
> position. EmEditor
> can edit files with the mixture of CR and LF as newline characters. Pressing the
> ENTER key inserts the same newline character at the current line, CR only, LF
> only or CR+LF. This command always inserts CR+LF no matter what newline character is used at the current line.

### How to Run

- Default Menu: **Insert** \> **CR and LF**
- [All Commands](../tools/all_commands): **Insert** \> **CR and LF**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_INSERT\_CR\_LF (4274)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4274);

#### \[VBScript\]

> editor.ExecuteCommandByID 4274
