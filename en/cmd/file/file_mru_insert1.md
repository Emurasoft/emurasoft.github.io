# List of Recent Files to Insert command

## Summary

Inserts a specified recently accessed file at the cursor position (multiple items).

## Description

This command consists of multiple menu items, allowing you choose a recently
accessed file to insert at the cursor position. The number of files to be
displayed as the recent files can be set on the
**Number of Recent**
**Files** text box on the
[**History** page](../../dlg/customize/history/index) of
the [**Customize** dialog box](../../dlg/customize/index),
under the **Tools** Menu (**Tools** \> **Customize** \> **History**).

## How to Run

- Default Menu: **Insert** \> **(select file name)**
- [All Commands](../tools/all_commands): **Insert** \> **(select file name)**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_FILE_MRU_INSERT1 through EEID_FILE_MRU_INSERT1 + 63 (from 4864
```
through 4864 + 63)

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4864 + i); // i is an integer from 0 through 63
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4864 + i   ' i is an integer from 0
through 63
```
