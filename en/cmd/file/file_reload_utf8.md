# Reload as UTF-8 command

## Summary

Reloads the current file using Unicode (UTF-8) encoding.

## Description

This command reloads the current file from the disk using the Unicode (UTF-8)
encoding. If the document is changed within EmEditor, the prompt message
"Are you sure you want to abandon changes?" appears. Selecting **Yes**
will discard the changes without saving, and will reload the new contents.
Selecting **No** will abort reloading and will allow you to continue
editing the document.

## How to Run

- Default Menu: **File** \> **Reload** \> **UTF-8**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **UTF-8**
- Toolbar: ![](../../images/reload.gif) (on
the arrow) > **UTF-8**
- Status Bar: (double-click on **Encodings**) \> **UTF-8**
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_RELOAD_UTF8 (4258)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4258);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4258
```
