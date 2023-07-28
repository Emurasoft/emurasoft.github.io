# Convert to CSV (multiple items) command

## Summary

Converts the current separated value document or fixed width column document to the specified separated value document (multiple items).

## Description

Converts the current separated value document or fixed width column document to the specified separated value document.

## How to Run

- Default Menu: (None)
- [All Commands](../tools/all_commands): **CSV** \> **Convert to** \> **(CSV)**
- Toolbar: (None)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
From EEID_CONVERT_TO_SV through EEID_CONVERT_TO_SV + 63 (from 22656 through 22656 + 63)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(22656 + i); //i is an integer from 0 through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22656 + i 'i is an integer from 0 through 63
```
