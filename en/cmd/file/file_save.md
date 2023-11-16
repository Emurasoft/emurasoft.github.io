# Save command

## Summary

Saves the current file.

## Description

This command saves the document with the current file name unless the document
is untitled. If you want to change the encoding or the return
method, select the [**Save As** command](file_save_as) or
the [**Save with Encoding (multiple menu)** command](file_save_defined).

If the file is untitled, the **Save As** dialog box will be displayed, which allows you to enter a file name.

## How to Run

- Default Menu: **File** \> **Save**
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save**
- Toolbar: ![](../../images/filesave.gif)
- Status Bar: None
- Default Shortcut Key: CTRL+S

## Plug-in Command ID

```
EEID_FILE_SAVE (4099)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4099);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4099
```
