# Logical End command

## Summary

Moves the cursor to the end of the current logical line.

## Description

Moves the cursor to the end of the current logical line.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Logical End**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: ALT+END

## Plug-in Command ID

```
EEID_LOGICAL_END (4167)```

## Macros

### \[JavaScript\]

```
document.selection.EndOfLine(false,eeLineLogical);
```

### \[VBScript\]

```
document.selection.EndOfLine false,eeLineLogical
```
