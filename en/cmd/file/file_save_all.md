# Save All command

### Summary

> Saves all currently open files.

### Description

> This command selects the [**Save** \
> command](file_save) for all opened EmEditor windows. If an untitled file exists,
> the **Save As** dialog box appears, which allows you to enter a file name to save the file as.

### How to Run

- Default Menu: **File** \> **Save All**
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save All**
- Toolbar:
![](../../images/filesaveall.gif)
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_FILE\_SAVE\_ALL (4101)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4101);

#### \[VBScript\]

> editor.ExecuteCommandByID 4101
