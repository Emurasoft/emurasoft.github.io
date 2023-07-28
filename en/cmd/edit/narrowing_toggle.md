# Toggle Narrowing command

## Summary

Sets or resets only the selection as editable area and makes the rest inaccessible.

## Description

Sets or resets only the selection (whole logical lines including the
selection) as editable area and make the rest inaccessible.

## How to Run

- Default Menu: **Edit** \> **Narrowing**
- [All Commands](../tools/all_commands): **Edit** \> **Narrowing** \> **Toggle Narrowing**
- Toolbar: ![](../../images/narrowing.gif)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_NARROWING_TOGGLE (4456)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4456);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4456
```
