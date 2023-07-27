# New and Paste command

## Summary

Creates a new file and inserts the contents of the Clipboard.

## Description

This command is equivalent to the [New Text \
command](file_new) followed by the [Paste \
command](../edit/edit_paste). By default, the new file will use the Text configuration. You can change the default configuration in the
[Define Configurations dialog box](../../dlg/configurations/index).

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>New \>New and Paste
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_NEW_PASTE (4123)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4123);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4123
```
