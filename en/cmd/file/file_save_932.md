# Save as Japanese Shift JIS command

## Summary

Saves the current file using Japanese Shift JIS encoding.

## Description

This command saves the current file using the
Japanese Shift JIS encoding, unless the document is untitled. If the file is
untitled, the **Save As** dialog box will be displayed,
which allows you to enter a file name to save the file as.

This command remains for compatibility with the older versions of
EmEditor. You can use the [**Save with**\
**Encoding (multiple menu)** command](file_save_defined) instead and specify Japanese Shift
JIS.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save with Encoding** \> **Save as Japanese Shift JIS**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_SAVE_932 (4265)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4265);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4265
```
