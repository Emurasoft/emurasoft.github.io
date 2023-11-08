# Remove Empty Columns command

## Summary

Removes empty columns in the CSV document.

## Description

Removes empty columns in the CSV document. An empty column means that all the cells in the column are either empty or only two quotation marks defined for the specified CSV format, usually "". This command checks all columns even if the selection exists.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Convert** \> **Remove Empty Columns**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_REMOVE_EMPTY_COLUMNS (4062)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4062);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4062
```
