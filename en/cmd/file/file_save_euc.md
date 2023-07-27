# Save as Japanese EUC command

## Summary

Saves the current file using Japanese EUC encoding.

## Description

This command saves the current file using the
Japanese EUC encoding, unless the document is untitled. If the document is
untitled, theSave As dialog box appears,
which allows you to enter a file name to save the file as.

This command remains for compatibility with the older versions of
EmEditor. You can use the [Save with\
Encoding (multiple menu) command](file_save_defined) instead and specify Japanese EUC.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Save
\>Save with Encoding \>Save as Japanese EUC
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_SAVE_EUC (4104)```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4104);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4104
```
