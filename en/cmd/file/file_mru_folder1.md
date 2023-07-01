# List of Recent Folders command

### Summary

> Opens a specified recently accessed folder (multiple items).

### Description

> This command consists of multiple menu items. With this command, you can
> choose a folder containing files which have been recently accessed to open. The number of folders to be
> displayed as the recently used folders can be set on the
> **Number of Recent**
> **Files** text box on the
> [**History** page](../../dlg/customize/history/index) of
> the [**Customize** dialog box](../../dlg/customize/index),
> under the **Tools** Menu ( **Tools** \> **Customize** \> **History**).

### How to Run

- Default Menu: **System Tray Icon menu** \> **Recent Folder** \> **(select folder**
**path)**
- [All Commands](../tools/all_commands): **File** \> **Open**
\> **Recent Folder** \> **(select folder path)**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- From EEID\_FILE\_MRU\_FOLDER1 through EEID\_FILE\_MRU\_FOLDER1 + 63 (from 4992
through 4992 + 63)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4992 + i);  // i is an integer from 0
> through 63

#### \[VBScript\]

> editor.ExecuteCommandByID 4992 + i   ' i is an integer from 0
> through 63
