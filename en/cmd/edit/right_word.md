# Word Right command

## Summary

Moves the cursor one word to the right.

## Description

Moves the cursor one word to the right. This command ignores white space,
and moves the cursor to the start of
the next word in the current line.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Word Right**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+RIGHT ARROW

## Plug-in Command ID

```
EEID_RIGHT_WORD (4158)```

## Macros

### \[JavaScript\]

```
document.selection.WordRight(false,1);
```

### \[VBScript\]

```
document.selection.WordRight false,1
```
