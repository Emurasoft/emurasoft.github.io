# Delete Left Character command

## Summary

Deletes the selection, or deletes one character at the left of the cursor.

## Description

Deletes the selected text (if any), or deletes one character to the
left of the cursor if no text is selected.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Delete
\>Delete Left Character
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: Backspace

## Plug-in Command ID

```
EEID_BACK (4186)```

## Macros

### \[JavaScript\]

```
document.selection.DeleteLeft(1);
```

### \[VBScript\]

```
document.selection.DeleteLeft 1
```
