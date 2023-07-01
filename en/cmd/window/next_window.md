# Next Document command

### Summary

> Switches to the next document.

### Description

> Switches to the next open EmEditor document. The behavior of this command depends on whether the
> [**Switch to last used document for Next**\
> **Document command** check box](../../dlg/customize/window/index) is checked. If it is checked, this command will switch to the last used document. If not checked, this command will switch to the next document displayed on the
> tab bar.

### How to Run

- Default Menu: **Window** \> **Next Document**
- [All Commands](../tools/all_commands): **Window**
\> **Document Navigation**
\> **Next Document**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: CTRL+TAB

### Plug-in Command ID

- EEID\_NEXT\_WINDOW (4245)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4245);

#### \[VBScript\]

> editor.ExecuteCommandByID 4245
