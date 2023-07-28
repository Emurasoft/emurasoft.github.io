# Save Workspace As command

## Summary

Saves the workspace as a new file name.

## Description

This command saves the full path names, the cursor positions, and other
settings of all currently open documents in EmEditor into a new workspace file. The [**Open Workspace** command](workspace_open) will
restore the positions and settings saved by this command.

## How to Run

- Default Menu: **File > Workspace** \> **Save As Workspace**
- [All Commands](../tools/all_commands): **File** \> **Workspace**
\> **Save As Workspace**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_WORKSPACE_SAVE_AS (3925)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(3925);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3925
```
