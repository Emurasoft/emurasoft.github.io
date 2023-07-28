# Word Left Extend command

## Summary

Extends the selection one word to the left.

## Description

Extends the selection one word to the left. If there are white space
characters
after the word, this command extends the selection to the start of the
previous word.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Word Left Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+LEFT ARROW

## Plug-in Command ID

```
EEID_SHIFT_LEFT_WORD (4175)```

## Macros

### \[JavaScript\]

```
document.selection.WordLeft(true,1);
```

### \[VBScript\]

```
document.selection.WordLeft true,1
```
