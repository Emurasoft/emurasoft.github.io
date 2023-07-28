# Close All Others command

## Summary

Closes all open files except the currently working file.

## Description

This command closes all opened files except the currently working file. If a modified file exists, a prompt message appears to select whether you want to save the changes.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Close**
\> **Close All Others**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_CLOSE_ALL_OTHERS (4384)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4384);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4384
```
