# Logical End Extend command

## Summary

Extends the selection to the end of the current logical line.

## Description

Extends the selection to the end of the current logical line.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Logical End Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: ALT+SHIFT+END

## Plug-in Command ID

```
EEID_SHIFT_LOGICAL_END (4183)```

## Macros

### \[JavaScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
```

### \[VBScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
```
