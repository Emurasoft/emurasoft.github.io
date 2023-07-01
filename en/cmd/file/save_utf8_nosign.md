# Save as UTF-8 without Signature command

### Summary

> Saves the current file using Unicode (UTF-8) encoding without signature.

### Description

> This command saves the document with the current file name using the Unicode (UTF-8) encoding without signature, unless the document is untitled. If the document is untitled, the **Save As** dialog box appears,
> which allows you to enter a file name to save the file as.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save with Encoding** \> **Save as UTF-8 without Signature**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_SAVE\_UTF8\_NOSIGN (4488)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4488);

#### \[VBScript\]

> editor.ExecuteCommandByID 4488
