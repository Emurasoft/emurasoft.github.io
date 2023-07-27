# New and Paste in Quotes command

## Summary

Creates a new file and inserts the contents of the Clipboard in quotes.

## Description

This command is equivalent to the [New Text \
command](file_new) followed by the [Paste in\
Quotes command](../edit/paste_prefix). By default, the new file will use the Text configuration. You can change the default configuration at the
[Define Configurations dialog box](../../dlg/configurations/index).

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>New \>New and Paste in Quotes
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_NEW_PASTE_PREFIX (4271)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4271);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4271
```
