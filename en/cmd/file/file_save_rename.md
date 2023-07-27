# Rename command

## Summary

Renames the current file.

## Description

Unlike the [Save As command](file_save_as), this
command renames the current file, then deletes the old file if the old file exists. If the document has been saved into a file before, this command displays the
Save As dialog box, which allows you to enter a file name to save the
currently opened file. After you specify a new file name, the prompt
message "Are you sure you want to delete ...?" appears. SelectingYes
will delete the file with the previous name. SelectingNo will not
delete the previous name, but save the file as the new name, equivalent to
the behavior of the [Save As command](file_save_as). If the document has never been saved into a file, theRename dialog box appears instead, where you can change the document title without saving it into a file.

If you want to save the file as a different name but do not want to
delete the previous file, use the [Save As \
command](file_save_as) instead.

## How to Run

- Default Menu:File \>Rename
- [All Commands](../tools/all_commands):File \>Save
\>Rename
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_SAVE_RENAME (4252)```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4252);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4252
```
