# Save Newline Characters as CR+LF command

### Summary

> Saves newline characters as CR+LF.

### Description

> This command saves the document after converting all newline characters into CR+LF
> (Windows). If the document is untitled, the **Save As** dialog box appears,
> which allows you to enter a file name to save the file as.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save in Different Newline Characters** \> **Save as CR+LF**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_SAVE\_AS\_CRLF (4105)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4105);

#### \[VBScript\]

> editor.ExecuteCommandByID 4105