# List of New Configurations command

### Summary

> Creates a new file with a specified configuration (multiple items).

### Description

> This command consists of multiple menu items. You can select from the predefined
> configurations. This command creates a new file with the specified
> configuration. You can edit, delete, or add configurations in the
> [**Define Configurations** dialog box](../../dlg/configurations/index).

### How to Run

- Default Menu: **File** \> **New** \> **(configuration name)**
- [All Commands](../tools/all_commands): **File** \> **New > (configuration name)**
- Toolbar: ![](../../images/filenew.gif) (on
the arrow) + (configuration name)
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- From EEID\_FILE\_NEW\_CONFIG through ID\_FILE\_NEW\_CONFIG + 255 (from 7168
through 7168 + 255)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(7168 + i);  // i is an integer from 0
> through 255

#### \[VBScript\]

> editor.ExecuteCommandByID 7168 + i  ' i is an integer from 0 through 255