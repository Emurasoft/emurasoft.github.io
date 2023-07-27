# Save as UTF-8 command

## Summary

Saves the current file using Unicode (UTF-8) encoding.

## Description

This command saves the document with the current file name using the Unicode (UTF-8) encoding, unless the document is untitled. If the document is untitled, theSave As dialog box appears,
which allows you to enter a file name to save the file as.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Save
\>Save with Encoding \>Save as UTF-8
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_SAVE_UTF8 (4255)```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4255);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4255
```
