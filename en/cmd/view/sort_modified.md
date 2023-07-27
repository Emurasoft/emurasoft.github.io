# Arrange by Modified command

## Summary

Arranges tabs by modified time.

## Description

Arranges tabs by time of last modification (most recently modified appears to the left). If the [Auto Arrange command](auto_sort) is checked, this command is called each time when a file is opened or saved as a name, and automatically arranged. If the
[Auto Arrange command](auto_sort) is not checked, this command is called once.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):View \>Arrange Tabs by
\>Modified
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_SORT_MODIFIED (4400)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4400);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4400
```
