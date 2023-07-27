# Delete command

## Summary

Deletes the selection, or deletes one character to the right of the cursor.

## Description

Deletes the selected text (if any), or deletes one character to the
right of the cursor if no text is selected.

## How to Run

- Default Menu:Edit \>Delete
- [All Commands](../tools/all_commands):Edit \>Delete
\>Delete Right Character
- Toolbar: ![](../../images/delete.gif)
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+BACKSPACE or DELETE

## Plug-in Command ID

```
EEID_DELETE (4135)```

## Macros

### \[JavaScript\]

```
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.Delete 1
```
