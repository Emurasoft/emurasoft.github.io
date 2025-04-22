# Replace in Files command

## Summary

Replaces text in multiple files.

## Description

Replaces a common string in multiple files. This command will display the
[**Replace in Files** dialog box](../../dlg/replace_in_files/index).
Specifying a string to find, a string to replace with, file types, a folder
to search, and other options, will start replacing in files. If the
**Keep Modified Files**
**Open** check box is checked, changes to files will not be made immediately, but all files that have had replacements made will be left open, so changes can be undone in each file, using the Undo command.

## How to Run

- Default Menu: **Search** \> **Replace in Files**
- [All Commands](../tools/all_commands): **Search**
\> **Replace in Files**
- Toolbar: ![](../../images/replaceinfiles.png)
- Status Bar: None
- Default Shortcut Key: CTRL+SHIFT+H

## Plug-in Command ID

```
EEID_REPLACE_IN_FILES (4362)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4362);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4362
```
