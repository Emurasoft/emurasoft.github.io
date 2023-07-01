# Save All with Encoding command

### Summary

> Saves all opened documents with the specified destination folder,
> encoding, and newline characters, except for untitled documents.

### Description

> This command displays the **Save All with Encoding** dialog box, where you can specify options for saving all open files (except untitled documents) with a specified encoding. The
> dialog box allows you to choose the destination folder, the encoding to save in, and the newline characters.
>
> In order to use this command, the opened documents that you wish to save with this command must have been previously saved. In other words, you cannot use the **Save All with Encoding** command for untitled documents that have not yet been created using the **Save** or **Save As** commands.

### How to Run

- Default Menu: **File** \> **Save All with Encoding**
- [All Commands](../tools/all_commands): **File** \> **Save All with Encoding**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_FILE\_SAVE\_ALL\_AS (3843)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(3843);

#### \[VBScript\]

> editor.ExecuteCommandByID 3843
