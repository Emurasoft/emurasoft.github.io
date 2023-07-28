# Split Lines command

## Summary

Splits lines by inserting newline characters and removing trailing spaces.

## Description

Splits lines by inserting newline characters and removing trailing spaces. Similar to [**Insert newline characters** command](insert_cr_wrap), but this command removes a space at each line before the newline character. The newline character will
match to the method used at the current line.

## How to Run

- Default Menu: **Convert** \> **Split Lines**
- [All Commands](../tools/all_commands): **Convert** \> **Split Lines**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_SPLIT_LINES (4379)```

## Macros

### \[JavaScript\]

```
document.selection.Format(eeFormatSplitLines);
```

### \[VBScript\]

```
document.selection.Format eeFormatSplitLines
```
