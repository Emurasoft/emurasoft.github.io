# Undo Recent (multiple items) command

## Summary

Undo through the specified action.

## Description

Undo through the specified action.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Undo \>Undo Recent (multiple items)
- Toolbar: ![](../../images/editundo.gif) (on the arrow)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
From EEID_UNDO_RECENT through EEID_UNDO_RECENT + 63 (from 22848 through 22848 + 63)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(22848 + i); //i is an integer from 0 through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22848 + i 'i is an integer from 0 through 63
```
