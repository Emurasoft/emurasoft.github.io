# Close and Open command

## Summary

Closes the current file and opens another existing file.

## Description

This command displays the **Open** dialog box, and allows you to select
a file you would like to open with EmEditor. After a file is selected, a
prompt will be displayed asking whether save changes for previous file or not. Selecting either Yes or No will open
the selected file.

If the current EmEditor window is untitled and no character is inserted,
this command behaves the same as the [**Open** command](file_open).

## How to Run

- Default Menu: **File** \> **Close and Open**
- [All Commands](../tools/all_commands): **File** \> **Open**
\> **Close and Open**
- Toolbar:
![](../../images/filecloseopen.gif)
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_CLOSE_OPEN (4098)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4098);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4098
```
