# Page Down Extend command

## Summary

Extends the selection down one page.

## Description

Extends the selection down one page. The cursor moves a half page if theScroll Half Page check box is checked on the
[Scroll page](../../dlg/properties/scroll/index) of the Configuration Properties dialog box.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Move Cursor Vertically
\>Page Down
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+PAGE DOWN

## Plug-in Command ID

```
EEID_SHIFT_PAGEDOWN (4179)```

## Macros

### \[JavaScript\]

```
document.selection.PageDown(true,1);
```

### \[VBScript\]

```
document.selection.PageDown true,1
```
