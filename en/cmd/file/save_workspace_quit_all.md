# Save Workspace and Close All command

### Summary

> Saves the workspace and closes all open files.

### Description

> This command saves the full path names, the cursor positions, and other
> settings of all currently open documents in EmEditor, then closes all open
> documents. This command is equivalent to the [Save \
> Workspace command](save_workspace) followed by the [Close All command](exit_all).

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Close**
\> **Save Workspace and Close All**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_SAVE\_WORKSPACE\_QUIT\_ALL (4332)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4332);

#### \[VBScript\]

> editor.ExecuteCommandByID 4332
