# Logical Home or Start of Text Extend command

## Summary

Extends the selection to the start of the current logical line, or the start
of the text on that line.

## Description

Extends the selection to the start of the current logical line. If there is
white space before any text, the selection is extended to the first
non-white space character on the current line.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Logical Home or Start of Text**
**Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_SHIFT_LOGICAL_HOME_TEXT (4334)```

## Macros

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineLogical | eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineLogical Or eeLineHomeText
```
