# Paste with Newline Characters command

### Summary

> Inserts the Clipboard contents and newline characters.

### Description

> Pastes the contents of the Clipboard, and Inserts newline characters at wrap points. Before this command, use the
> [**Copy** command](edit_copy) or the
> [**Cut** command](edit_cut) to put text on the Clipboard.
> This command uses the [**system default encoding**](../../glossary/systemdefaultencoding) if the
> **Always Paste as ANSI** check box
> on the [**General** page](../../dlg/properties/general/index) of the Properties dialog box is checked, or Unicode if not checked.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Paste**
\> **Paste with Newline Characters**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+J

### Plug-in Command ID

- EEID\_PASTE\_RETURN (4133)

### Macros

#### \[JavaScript\]

> document.selection.Paste(eeCopyNL);

#### \[VBScript\]

> document.selection.Paste eeCopyNL
