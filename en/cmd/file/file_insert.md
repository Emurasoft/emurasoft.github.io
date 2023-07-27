# Insert command

## Summary

Inserts a specified file at the current cursor position.

## Description

This command displays theInsert dialog box, which allows you to
select a file you want to insert into the current file. After a file is selected, this command
reads the selected file and inserts its contents at the cursor position.

## How to Run

- Default Menu:Insert \>Insert
- [All Commands](../tools/all_commands):Insert \>Insert
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_INSERT (4108)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4108);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4108
```
