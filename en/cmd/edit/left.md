# Char Left command

## Summary

Moves the cursor one character to the left.

## Description

Moves the cursor one character to the left. If the cursor is at the
beginning of a line, this command moves the cursor to the end of the previous line.
Equivalent to pushing the LEFT ARROW key once.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Char Left**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: LEFT ARROW

## Plug-in Command ID

```
EEID_LEFT (4157)```

## Macros

### \[JavaScript\]

```
document.selection.CharLeft(false,1);
```

### \[VBScript\]

```
document.selection.CharLeft false,1
```
