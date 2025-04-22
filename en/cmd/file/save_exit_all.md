# Save and Close All command

## Summary

Saves and Close all open files.

## Description

Saves and closes all open files. This command is equivalent to the
[**Save All** command](file_save_all) followed by the
[**Close All** command](exit_all).

## How to Run

- Default Menu: **File** \> **Save and Close All**
- [All Commands](../tools/all_commands): **File** \> **Close**
\> **Save and Close All**
- Toolbar: ![](../../images/saveexitall.png)
- Status Bar: None
- Default Shortcut Key: CTRL+SHIFT+E

## Plug-in Command ID

```
EEID_SAVE_EXIT_ALL (4118)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4118);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4118
```
