# Reload as UTF-7 command

## Summary

Reloads the current file using Unicode (UTF-7) encoding.

## Description

This command reloads the current file from the disk using the Unicode (UTF-7)
encoding. If the document is changed within EmEditor, the prompt message
"Are you sure you want to abandon changes?" appears. Selecting **Yes**
will discard the changes without saving, and will reload the new contents.
Selecting **No** will abort reloading and will allow you to continue
editing the document.

## How to Run

- Default Menu: **File** \> **Reload** \> **UTF-7**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **UTF-7**
- Toolbar: ![](../../images/reload.gif) (on
the arrow) > **System Default**
- Status Bar: (double-click on **Encodings**) \> **UTF-7**
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_RELOAD_UTF7 (4259)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4259);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4259
```
