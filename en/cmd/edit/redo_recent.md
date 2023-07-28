# Redo Recent (multiple items) command

## Summary

Redo through the specified action.

## Description

Redo through the specified action.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Redo** \> **Redo Recent (multiple items)**
- Toolbar: ![](../../images/editredo.gif) (on the arrow)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
From EEID_REDO_RECENT through EEID_REDO_RECENT + 63 (from 22912 through 22912 + 63)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(22912 + i); //i is an integer from 0 through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22912 + i 'i is an integer from 0 through 63
```
