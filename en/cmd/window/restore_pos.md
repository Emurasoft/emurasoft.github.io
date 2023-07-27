# Restore Window Position command

## Summary

Restores the window to the previously saved position.

## Description

This command restores the window to the previously saved position. Before this command can be used, the window position must be saved by pressing
Save
Current Window Size button on the [Window page](../../dlg/customize/window/index) of the
[Customize dialog box](../../dlg/customize/index).

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Window
\>Restore \>Restore Window Position
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: CTRL + 9

## Plug-in Command ID

```
EEID_RESTORE_POS (4406)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4406);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4406
```
