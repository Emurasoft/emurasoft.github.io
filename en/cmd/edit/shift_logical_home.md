# Logical Home Extend command

## Summary

Extends the selection to the start of the current logical line.

## Description

Extends the selection to the start of the current logical line.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Logical Home Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: ALT+SHIFT+HOME

## Plug-in Command ID

```
EEID_SHIFT_LOGICAL_HOME (4181)```

## Macros

## \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineLogical);
```

## \[VBScript\]

```
document.selection.StartOfLine true,eeLineLogical
```
