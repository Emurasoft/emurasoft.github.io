# Tag Jump command

## Summary

Jumps to a tag.

## Description

This command is used after running the [**Find** **in Files** command](../search/grep), or for parsing an error log to locate a string or an error. If
a file's path and a line number are displayed at the start of a line, this command will open the file and jump to the line
number in question.

## How to Run

- Default Menu: **Edit** \> **Advanced** \> **Tag Jump**
- [All Commands](../tools/all_commands): **Edit** \> **Advanced**
\> **Tag Jump**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: F10

## Plug-in Command ID

```
EEID_TAG_JUMP (4147)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4147);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4147
```
