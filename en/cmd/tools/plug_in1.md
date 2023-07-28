# Plug-ins List command

## Summary

Runs a specified plug-in (multiple items).

## Description

This command consists of multiple menu items. This command runs the
specified plug-in. The available plug-ins are defined in the
[**Customize Plug-ins** dialog box](../../dlg/plugins/index).

## How to Run

- Default Menu: **Plug-ins** \> **(plug-in name)**
- [All Commands](all_commands): **Plug-ins** \> **(plug-in name)**
- Toolbar: each button on the Plug-ins toolbar
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_PLUG_IN1 through EEID_PLUG_IN1 + 255 (from 5632 through 5632 +```
255)

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(5632+i);  // i is an integer from 0 through
255
```

## \[VBScript\]

```
editor.ExecuteCommandByID 5632+i  ' i is an integer from 0 through 255
```
