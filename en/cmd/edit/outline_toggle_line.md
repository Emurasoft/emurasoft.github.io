# Expand/Collapse Line command

## Summary

Expands or collapses the current line while outlining is displayed.

## Description

While outlining is displayed, if the current line is collapsed, this command expands the current line, and if the current line is expanded, this command collapses the current line. It is the same effect as clicking the "+" button or the "-"
button at the left side of a text line. A plug-in for outlining is necessary to display the outlining.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Outlining \>Expand/Collapse Line
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_OUTLINE_TOGGLE_LINE (4412)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4412);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4412
```
