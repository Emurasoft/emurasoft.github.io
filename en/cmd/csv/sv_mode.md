# CSV (multiple items) command

## Summary

Shows the document as the specified separated value mode (multiple items).

## Description

Shows the document as the specified separated value mode.

## How to Run

- Default Menu: **CSV** \> **(CSV)**
- [All Commands](../tools/all_commands): **CSV** \> **(CSV)**
- Toolbar: ![](../../images/csv_mode.png) (CSV)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
From EEID_SV_MODE through EEID_SV_MODE + 63 (from 22528 through 22528 + 63)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(22528 + i); //i is an integer from 0 through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22528 + i 'i is an integer from 0 through 63
```
