# Restore Default Workspace command

### Summary

> Restores the saved default workspace state.

### Description

> This command restores the full path names, the cursor positions, and other settings of all currently open documents in EmEditor to a previously saved
> state set by the [**Save Default Workspace** command](save_workspace).

### How to Run

- Default Menu: **System Tray Icon menu** \> **Restore Default Workspace**
- [All Commands](../tools/all_commands): **File** \> **Workspace**
\> **Restore Default Workspace**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: ALT+0

### Plug-in Command ID

- EEID\_LOAD\_WORKSPACE (4329)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4329);

#### \[VBScript\]

> editor.ExecuteCommandByID 4329
