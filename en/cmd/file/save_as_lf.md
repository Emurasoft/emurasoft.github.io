# Save Newline Characters as LF Only command

## Summary

Saves newline characters as LF only.

## Description

This command saves the document after converting all newline characters into LF only
(Unix). If the document is untitled, theSave As dialog box appears,
which allows you to enter a file name to save the file as.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Save
\>Save in Different Newline Characters \>Save as LF
only
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_SAVE_AS_LF (4107)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4107);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4107
```
