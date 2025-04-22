# List of Encodings to Reload command

## Summary

Reloads the current file with a specified encoding (multiple items).

## Description

This command consists of multiple menu items. You can select from predefined
encodings.
This command reloads the currently opened file from the disk using the
specified encoding. If the document is changed within
EmEditor, the prompt message "Are you sure you want to abandon changes?"
appears. Selecting **Yes** will abandon the changes without saving, and
will reload the new contents. Selecting **No** will abort reloading and
will allow you to continue editing the document.

## How to Run

- Default Menu: **File** \> **Reload** \> **(encoding)**
- [All Commands](../tools/all_commands): **File** \> **Reload** \> **(encoding)**
- Toolbar: ![](../../images/reload.png) (on
the arrow) -
(encoding)
- Status Bar: double-click on Encodings - (encoding)
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_FILE_RELOAD_DEFINED through EEID_FILE_RELOAD_DEFINED + 255 (from 6656
```
through
6656 + 255)

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(6656 + i);  // i is an integer from 0
through 255
```

## \[VBScript\]

```
editor.ExecuteCommandByID 6656 + i  ' i is an integer from 0
through 255
```
