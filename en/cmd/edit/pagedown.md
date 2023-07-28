# Page Down command

## Summary

Moves the cursor down one page.

## Description

Moves the cursor down one page at a time. The cursor will move down half of a
page if the **Scroll Half Page** check box is checked on the
[**Scroll** page](../../dlg/properties/scroll/index) in the Configuration Properties dialog box.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Vertically**
\> **Page Down**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: PAGE DOWN

## Plug-in Command ID

```
EEID_PAGEDOWN (4163)```

## Macros

### \[JavaScript\]

```
document.selection.PageDown(false,1);
```

### \[VBScript\]

```
document.selection.PageDown false,1
```
