# Tools List command

### Summary

> Launches a specified tool (multiple items).

### Description

> This command consists of multiple menu items. This command launches a
> specified tool. The available tools can be defined in the
> [**External Tools** dialog box](../../dlg/tools/index).

### How to Run

- Default Menu: **Tools** \> **External Tools** \> **(tool name)**
- [All Commands](all_commands): **External Tools**
\> **(tool name)**
- Toolbar: Each button on the Tools toolbar
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- From EEID\_TOOL1 through EEID\_TOOL1 + 255 (from 8192 through 8192 + 255)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(8192+i);  // i is an integer from 0 through
> 255

#### \[VBScript\]

> editor.ExecuteCommandByID 8192+i  ' i is an integer from 0 through 255
