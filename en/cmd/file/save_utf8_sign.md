# Save as UTF-8 with Signature command

## Summary

Saves the current file using Unicode (UTF-8) encoding with signature.

## Description

This command saves the document with the current file name using the Unicode (UTF-8) encoding with signature, unless the document is untitled. If the document is untitled, theSave As dialog box appears,
which allows you to enter a file name to save the file as.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Save
\>Save with Encoding \>Save as UTF-8 with Signature
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_SAVE_UTF8_SIGN (4487)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4487);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4487
```
