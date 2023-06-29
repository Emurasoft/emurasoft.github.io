# Save Default Workspace command

### Summary

> Saves the default workspace.

### Description

> This command saves the full path names, the cursor positions, and other
> settings of all currently open documents in EmEditor. The
> [**Restore Default Workspace** command](load_workspace) will
> restore the positions and settings saved by this command.

### How to Run

- Default Menu: **System Tray Icon menu** \> **Save Default Workspace**
- [All Commands](../tools/all_commands): **File** \> **Workspace**
\> **Save Default Workspace**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: CTRL+SHIFT+0

### Plug-in Command ID

- EEID\_SAVE\_WORKSPACE (4330)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4330);

#### \[VBScript\]

> editor.ExecuteCommandByID 4330