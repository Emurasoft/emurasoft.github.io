# Save as Binary (Hex View) command

### Summary

> Saves the current file using Binary (Hex View) encoding.

### Description

> This command saves the current file using the Binary (Hex View) encoding, unless the
> document is untitled. If the document is untitled, the **Save As** dialog box appears,
> which allows you to enter a file name to save the file as.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save with Encoding** \> **Save as Binary (Hex View)**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_FILE\_SAVE\_HEX (4441)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4441);

#### \[VBScript\]

> editor.ExecuteCommandByID 4441