# Find in Files command

### Summary

> Searches multiple files for a matching string.

### Description

> Searches multiple files for a matching string. This command displays the
> [**Find in Files** dialog box](../../dlg/find_in_files/index).
> Specifying a string to search, file types, a folder to search, and other
> options will start finding a string in multiple files in a specified folder.
> The result of this command will be the list of full file paths and the line
> number the search query occurs on. Using the [**Tag Jump** command](../edit/tag_jump) with the results will jump to the searched string within the searched files.

### How to Run

- Default Menu: **Search** \> **Find in Files**
- [All Commands](../tools/all_commands): **Search**
\> **Find in Files**
- Toolbar: ![](../../images/grep.gif)
- Status Bar: None
- Default Shortcut Key: CTRL+SHIFT+F

### Plug-in Command ID

- EEID\_GREP (4207)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4207);

#### \[VBScript\]

> editor.ExecuteCommandByID 4207