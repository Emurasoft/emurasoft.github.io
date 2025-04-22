# Reload as System Default Encoding command

## Summary

Reloads the current file using the
[system default encoding](../../glossary/index).

## Description

This command reloads the current file from the disk using the
[system default encoding](../../glossary/index). If the document is changed within EmEditor, the prompt message
"Are you sure you want to abandon changes?" appears. Selecting **Yes**
will discard the changes without saving, and will reload the new contents.
Selecting **No** will abort reloading and will allow you to continue
editing the document.

## How to Run

- Default Menu: **File** \> **Reload** \> **System Default**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **System Default**
- Toolbar: ![](../../images/reload.png) (on
the arrow) > **System Default**
- Status Bar: (double-click on **Encodings**) \> **System Default**
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_RELOAD_ANSI (4110)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4110);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4110
```
