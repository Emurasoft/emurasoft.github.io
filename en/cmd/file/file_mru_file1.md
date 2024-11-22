# List of Recent Documents command

## Summary

Opens a specified recently accessed document (multiple items).

## Description

This command consists of multiple menu items, displaying a list of recently
accessed
files. This command opens a specified file. The number of files to be
displayed as the recent files can be set on the
**Number of Recent**
**Files** text box on the
[**History** page](../../dlg/customize/history/index) of
the [**Customize** dialog box](../../dlg/customize/index),
under the **Tools** Menu (**Tools** \> **Customize** \> **History**).

## How to Run

- Default Menu: **File** > **(select file name)**
- [All Commands](../tools/all_commands): **File** \> **Open**
\> **Recent File** \> **(select file name)**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_FILE_MRU_FILE1 through EEID_FILE_MRU_FILE1 + 63 (from 4609 through 4609 + 63)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID (4609 + i);  // i is an integer from 0
through 63
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4609 + i  ' i is an integer from 0 through
63
```
