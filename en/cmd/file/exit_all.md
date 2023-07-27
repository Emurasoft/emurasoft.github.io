# Close All command

## Summary

Closes all open files and quits EmEditor.

## Description

This command closes all opened files. If a modified file exists, a prompt
message appears to select whether you want to save the changes or not.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Close
\>Close All
- Toolbar: ![](../../images/exitall.gif)
- Status Bar: None
- Default Shortcut Key: ALT+SHIFT+X

## Plug-in Command ID

```
EEID_EXIT_ALL (4119)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4119);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4119
```
