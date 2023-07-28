# Char Right command

## Summary

Moves the cursor one character to the right.

## Description

Moves the cursor one character to the right. If the cursor is at the end of a
line, this command moves the cursor to the start of the next line.
Equivalent to pushing the RIGHT ARROW key once.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Char Right**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: RIGHT ARROW

## Plug-in Command ID

```
EEID_RIGHT (4156)```

## Macros

### \[JavaScript\]

```
document.selection.CharRight(false,1);
```

### \[VBScript\]

```
document.selection.CharRight false,1
```
