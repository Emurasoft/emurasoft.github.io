# Delete Right Line command

## Summary

Deletes the line to the right of the cursor.

## Description

Deletes text from the cursor position to the end of the logical line at the
cursor.

## How to Run

- Default Menu: **Edit** \> **Advanced** \> **Delete Right Line**
- [All Commands](../tools/all_commands): **Edit** \> **Delete**
\> **Delete Right Line**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_DELETE_RIGHT_LINE (4191)```

## Macros

### \[JavaScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.EndOfLine true,eeLineLogical
document.selection.Delete 1
```
