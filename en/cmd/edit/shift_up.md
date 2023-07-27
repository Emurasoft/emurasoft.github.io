# Line Up Extend command

## Summary

Extends the selection up one line.

## Description

Extends the selection up one line. If no text is selected, this command will select the line directly above the cursor position.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Extend Selection
\>Line Up Extend
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: Shift+UP ARROW

## Plug-in Command ID

```
EEID_SHIFT_UP (4176)```

## Macros

### \[JavaScript\]

```
document.selection.LineUp(true,1);
```

### \[VBScript\]

```
document.selection.LineUp true,1
```
