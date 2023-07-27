# Configurations List command

## Summary

Selects a specified configuration (multiple items).

## Description

This command consists of multiple menu items. This command selects the
specified configuration as the current configuration. The current
configuration is displayed on the Status Bar. EmEditor defaults to the
Text configuration when a new document is created.

## How to Run

- Default Menu:Tools \>Select Configuration \> (configuration name)
- [All Commands](all_commands):Tools >
Select Configuration \> (configuration name)
- Toolbar: ![](../../images/configpopup.gif) (on
the arrow) >
(configuration name)
- Status Bar: (double-click on configuration name) > (configuration name)
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_SELECT_CONFIG through EEID_SELECT_CONFIG + 255 (from 5120```
through 5120 + 255)

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(5120 + i);  // i is an integer from 0
through 255
```

### or

document.ConfigName = "(configuration name)";

### \[VBScript\]

```
editor.ExecuteCommandByID 5120 + i   ' i is an integer from 0
through 255
```

### or

document.ConfigName = "(configuration name)"
