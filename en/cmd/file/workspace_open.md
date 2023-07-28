# Open Workspace command

## Summary

Opens a saved workspace file.

## Description

This command opens a workspace file to restore the full path names, the cursor positions, and other settings of all currently open documents in EmEditor to a previously saved file set by the [**Save Workspace** command](workspace_save_current) or the [**Save Workspace As** command](workspace_save_as).

## How to Run

- Default Menu: **File** \> **Workspace** \> **Open Workspace**
- [All Commands](../tools/all_commands): **File** \> **Workspace**
\> **Open Workspace**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_WORKSPACE_OPEN (3924)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(3924);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3924
```
