# Save as Binary (ASCII View) command

## Summary

Saves the current file using Binary (ASCII View) encoding.

## Description

This command saves the current file using the Binary (ASCII View) encoding, unless the
document is untitled. If the document is untitled, theSave As dialog box appears,
which allows you to enter a file name to save the file as.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Save
\>Save with Encoding \>Save as Binary (ASCII View)
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_SAVE_BINARY (4440)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4440);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4440
```
