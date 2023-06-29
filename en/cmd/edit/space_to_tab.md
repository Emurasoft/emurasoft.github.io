# Tabify All command

### Summary

> Converts equivalent spaces to tabs throughout the entire document.

### Description

> Converts spaces at the start of all lines throughout the entire document into tabs.
> The converted number of spaces must be equal to the number of spaces set for
> a tab, which can be set in the [**Tab/Indent** dialog box](../../dlg/properties/general/indent/index). This is equivalent to the
> [**Tabify** command](tabify) after selecting the entire document, but this command does not extend the selection.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Advanced** \> **Tabify Document**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_SPACE\_TO\_TAB (4355)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4355);

#### \[VBScript\]

> editor.ExecuteCommandByID 4355