# Open command

## Summary

Opens an existing file.

## Description

This command displays the **Open** dialog box, and allows you to select a file you would like to open with EmEditor. Normally, the file will open in a new tab. However, the file will open within the current
tab if the current tab is untitled and no characters have been typed. If you wish to open a new file within the current tab every time, use the [**Close and Open** command](file_close_open).

## How to Run

- Default Menu: **File** \> **Open**
- [All Commands](../tools/all_commands): **File** \> **Open**
\> **Open**
- Toolbar: ![](../../images/fileopen.gif)
- Status Bar: None
- Default Shortcut Key: CTRL+O

## Plug-in Command ID

```
EEID_FILE_OPEN (4097)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4097);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4097
```
