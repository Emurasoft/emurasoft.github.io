# Cut Line(s) command

## Summary

Cuts the selected lines or current line and moves it to the Clipboard.

## Description

Cuts the selected lines or one logical line at the cursor, and puts it on the Clipboard. After
this command, you can place the line by moving the cursor to a
different location and running the [**Paste** command](edit_paste).

## How to Run

- Default Menu: **Edit** \> **Advanced** \> **Cut Line(s)**
- [All Commands](../tools/all_commands): **Edit** \> **Cut** \> **Cut Line(s)**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+L

## Plug-in Command ID

```
EEID_EDIT_CUT_LINE (4193)```

## Macros

### \[JavaScript\]

```
document.selection.SelectLine()
document.selection.Cut();
```

### \[VBScript\]

```
document.selection.SelectLine
document.selection.Cut
```
