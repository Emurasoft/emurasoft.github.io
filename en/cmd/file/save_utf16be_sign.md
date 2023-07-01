# Save as UTF-16BE with Signature command

### Summary

> Saves the current file using Unicode (UTF-16BE) encoding with signature.

### Description

> This command saves the current file using the Unicode (UTF-16BE) encoding with signature, unless the document is untitled.
> If the document is untitled, the **Save As** dialog box appears,
> which allows you to enter a file name to save the file as.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save with Encoding** \> **Save as UTF-16BE with Signature**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_SAVE\_UTF16BE\_SIGN (4485)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4485);

#### \[VBScript\]

> editor.ExecuteCommandByID 4485
