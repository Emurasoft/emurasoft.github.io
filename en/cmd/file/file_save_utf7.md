# Save as UTF-7 command

## Summary

Saves the current file using Unicode (UTF-7) encoding.

## Description

This command saves the current file using the Unicode (UTF-7) encoding, unless the
document is untitled. If the document is untitled, the **Save As** dialog box appears,
which allows you to enter a file name to save the file as.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save with Encoding** \> **Save as UTF-7**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_SAVE_UTF7 (4256)```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4256);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4256
```
