# Remove Newline Characters command

## Summary

Removes newline characters at wrap points in the selection.

## Description

Removes newline characters at wrap points in the selection. Similar to [Join Lines command](join_lines), but this command does not
insert a space at each line at wrap points.

## How to Run

- Default Menu:Convert \>Remove Newline Characters
- [All Commands](../tools/all_commands):Convert \>Remove Newline Characters
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_DELETE_CR_WRAP (4144)```

## Macros

### \[JavaScript\]

```
document.selection.Format(eeFormatDeleteNL);
```

### \[VBScript\]

```
document.selection.Format eeFormatDeleteNL
```
