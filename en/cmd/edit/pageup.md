# Page Up command

## Summary

Moves the cursor up one page.

## Description

Moves the cursor up one page at a time. The cursor will move up half of a page
if theScroll
Half Page check box is checked on the
[Scroll page](../../dlg/properties/scroll/index) in the Configuration Properties dialog box.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Move Cursor Vertically
\>Page Up
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: PAGE UP

## Plug-in Command ID

```
EEID_PAGEUP (4162)```

## Macros

## \[JavaScript\]

```
document.selection.PageUp(false,1);
```

## \[VBScript\]

```
document.selection.PageUp false,1
```
