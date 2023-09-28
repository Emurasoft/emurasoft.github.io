# Recent Workspace command

## Summary

Opens a specified recently used workspace (multiple items).

## Description

This command consists of multiple menu items, displaying a list of recently opened workspace
files. This command opens a specified workspace file to restore the full path names, the cursor positions, and other settings of all currently open documents in EmEditor to a previously saved file set by the [**Save Workspace** command](workspace_save_current) or the [**Save Workspace As** command](workspace_save_as). The number of files to be
displayed as the recent files can be set on the
**Number of Recent**
**Files** text box on the
[**History** page](../../dlg/customize/history/index) of
the [**Customize** dialog box](../../dlg/customize/index),
under the **Tools** Menu (**Tools** \> **Customize** \> **History**).

## How to Run

- Default Menu: **File** \> **Workspace** \> **(recent workspace)**
- [All Commands](../tools/all_commands): **File > Workspace > Recent Workspace > (recent workspace)**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_WORKSPACE_RECENT_FILE1 through EEID_WORKSPACE_RECENT_FILE1 + 63 (from 22784 through 22784 + 63)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID (22784 + i);  // i is an integer from 0
through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22784 + i  ' i is an integer from 0 through
63
```
