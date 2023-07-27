# Use One-Based Numerical Characters for Column Header command

## Summary

Uses one-based numerical characters for the column header.

## Description

Uses one-based numerical characters for the column header. This command is equivalent to the status where both theUse Alphabetical Characters for Column Header andUse Zero-Based Numerical Characters for Column Header check boxes are cleared in theCSV page of theCustomize dialog box.

## How to Run

- Default Menu:CSV \>Column Header Type \>1, 2, 3, ...
- [All Commands](../tools/all_commands):CSV \>Column Header Type \>1, 2, 3, ...
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_HEADER_NUM (3986)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(3986);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3986
```
