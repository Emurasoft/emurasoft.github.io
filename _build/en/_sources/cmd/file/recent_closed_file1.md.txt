# Recently Closed Files command

### Summary

> Opens a specified recently closed document (multiple items)

### Description

> This command consists of multiple menu items, displaying a list of recently
> closed
> files. This command opens a specified file. The number of files to be
> displayed as the recent files can be set on the
> **Number of Recent**
> **Files** text box on the
> [**History** page](../../dlg/customize/history/index) of
> the [**Customize** dialog box](../../dlg/customize/index),
> under the **Tools** Menu ( **Tools** \> **Customize** \> **History**).

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Open**
\> **Recently Closed File** \> **(select file name)**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- From EEID\_RECENT\_CLOSED\_FILE1 through EEID\_RECENT\_CLOSED\_FILE1 + 63 (from 4800 through 4800 + 63)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID (4800 + i);  // i is an integer from 0
> through 63

#### \[VBScript\]

> editor.ExecuteCommandByID 4800 + i  ' i is an integer from 0 through
> 63