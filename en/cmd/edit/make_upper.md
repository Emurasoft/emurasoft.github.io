# Uppercase command

### Summary

> Converts the selection to all uppercase characters.

### Description

> Converts the selection to all uppercase letters. For instance, a will become A, ä will
> become Ä, and λ will become Λ.

### How to Run

- Default Menu: **Convert** \> **Uppercase**
- [All Commands](../tools/all_commands): **Convert** \> **Uppercase**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+U

### Plug-in Command ID

- EEID\_MAKE\_UPPER (4149)

### Macros

#### \[JavaScript\]

> document.selection.ChangeCase(eeCaseUpperCase);

#### \[VBScript\]

> document.selection.ChangeCase eeCaseUpperCase