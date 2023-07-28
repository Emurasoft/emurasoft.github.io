# Word Left command

## Summary

Moves the cursor one word to the left.

## Description

Moves the cursor one word to the left. This command ignores white space,
and moves the cursor to the beginning of the previous word in the current line.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Word Left**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+LEFT ARROW

## Plug-in Command ID

```
EEID_LEFT_WORD (4159)```

## Macros

### \[JavaScript\]

```
document.selection.WordLeft(false,1);
```

### \[VBScript\]

```
document.selection.WordLeft false,1
```
