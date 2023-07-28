# Cut command

## Summary

Cuts the selection or the current line and moves it to the Clipboard.

## Description

Cuts the selected text and moves it to the Clipboard. After this command, you can place the selection by moving the cursor to a different location and run the [**Paste** command](edit_paste).

## How to Run

- Default Menu: **Edit** \> **Cut**
- [All Commands](../tools/all_commands): **Edit** \> **Cut**
\> **Cut**
- Toolbar: ![](../../images/cut.gif)
- Status Bar: None
- Default Keyboard Shortcut: CTRL+X or SHIFT+DELETE

## Plug-in Command ID

```
EEID_EDIT_CUT (4126)```

## Macros

### \[JavaScript\]

```
document.selection.cut();
```

### \[VBScript\]

```
document.selection.Cut
```
