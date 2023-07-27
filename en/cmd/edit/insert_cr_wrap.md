# Insert Newline Characters command

## Summary

Inserts newline characters at wrap points in the selection.

## Description

Inserts newline characters at wrap points in the selection. Similar to [Split Lines command](split_lines), but this command does not
remove a space at each line before the newline character. The newline character will
match to the newline character used at the current line.

## How to Run

- Default Menu:Convert >Insert Newline Characters
- [All Commands](../tools/all_commands):Convert >Insert Newline Characters
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_INSERT_CR_WRAP (4143)```

## Macros

## \[JavaScript\]

```
document.selection.Format(eeFormatInsertNL);
```

## \[VBScript\]

```
document.selection.Format eeFormatInsertNL
```
