# Auto Indent command

## Summary

Enables or disables the auto indent.

## Description

Enables or disables the auto indent. When auto indent is enabled, EmEditor will automatically indent newline characters to match the indent of the line immediately preceding the newline character.

## How to Run

- Default Menu: **View** \> **Tab/Indent** \> **Auto Indent**
- [All Commands](../tools/all_commands): **View** \> **Tab/Indent** \> **Auto Indent**
- Toolbar:
![](../../images/auto_indent24x16.png)
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_TOGGLE_AUTO_INDENT (4540)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4540);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4540
```
