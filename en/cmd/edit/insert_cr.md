# Insert CR command

### Summary

> Inserts a carriage return at the current cursor position.

### Description

> Inserts a carriage return (CR) at the current cursor position. EmEditor can edit files with
> the mixture of CR and LF as newline characters. Pressing the ENTER key inserts the
> same newline character at the current line, CR only, LF only or CR+LF. This
> command always inserts CR only, no matter what newline character is used at the
> current line.

### How to Run

- Default Menu: **Insert** \> **CR Only**
- [All Commands](../tools/all_commands): **Insert** \> **CR Only**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_INSERT\_CR (4145)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4145);

#### \[VBScript\]

> editor.ExecuteCommandByID 4145
