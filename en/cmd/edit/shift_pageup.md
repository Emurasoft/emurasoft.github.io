# Page Up Extend command

## Summary

Extends the selection up one page.

## Description

Extends the selection up one page. The cursor moves a half page
if theScroll
Half Page check box is checked on the
[Scroll page](../../dlg/properties/scroll/index) of the Configuration Properties dialog box.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Extend Selection
\>Page Up Extend
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+PAGE UP

## Plug-in Command ID

```
EEID_SHIFT_PAGEUP (4178)```

## Macros

### \[JavaScript\]

```
document.selection.PageUp(true,1);
```

### \[VBScript\]

```
document.selection.PageUp true,1
```
