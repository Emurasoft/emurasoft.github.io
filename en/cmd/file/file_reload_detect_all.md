# Reload Detect All command

## Summary

Reloads the current file using the best-fit encoding.

## Description

This command reloads the current file from the disk with an
encoding statistically detected from all encodings available on the Windows
Operating System. The detection may fail, especially when the file is small.
This command is available only when Internet Explorer 5.0 or later is
installed. If the document is changed within EmEditor, the prompt message
"Are you sure you want to abandon changes?" appears. Selecting **Yes**
will discard the changes without saving, and will reload the new contents.
Selecting **No** will abort reloading and will allow you to continue
editing the document.

## How to Run

- Default Menu: **File** \> **Reload** \> **Detect All**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **Detect All**
- Toolbar: ![](../../images/reload.png) (on
the arrow) > **Detect All**
- Status Bar: (double-click on **Encoding**) \> **Detect All**
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_RELOAD_DETECT_ALL (4279)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4279);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4279
```
