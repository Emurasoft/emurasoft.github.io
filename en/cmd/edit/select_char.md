# Select Character command

## Summary

Toggles character selection mode.

## Description

Toggles character selection mode. This command allows you to highlight
multiple characters with the keyboard.  Moving the cursor with the
arrow keys will expand or contract the
selection. Selecting the
[Copy command](edit_copy) or the
[Cut command](edit_cut) will end the character selection
mode.  This command is equivalent to holding down SHIFT and holding
down any of the arrow keys.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Extend Selection
\>Select Character
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: F8

## Plug-in Command ID

```
EEID_SELECT_CHAR (4153)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4153);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4153
```
