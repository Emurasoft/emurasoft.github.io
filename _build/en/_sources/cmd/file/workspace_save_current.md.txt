# Save Workspace command

### Summary

> Saves the workspace into the current workspace file.

### Description

> This command saves the full path names, the cursor positions, and other
> settings of all currently open documents in EmEditor into the current workspace file. The [**Open Workspace** command](workspace_open) will
> restore the positions and settings saved by this command.

### How to Run

- Default Menu: **File > Workspace** \> **Save Workspace**
- [All Commands](../tools/all_commands): **File** \> **Workspace**
\> **Save Workspace**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_WORKSPACE\_SAVE\_CURRENT (3926)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(3926);

#### \[VBScript\]

> editor.ExecuteCommandByID 3926