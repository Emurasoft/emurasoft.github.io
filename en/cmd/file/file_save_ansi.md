# Save as System Default Encoding command

## Summary

Saves the current file using the
[system default encoding.](../../glossary/index)

## Description

This command saves the document with the current file name using the
[system default encoding](../../glossary/index)
unless the document is untitled.
If the document is untitled, the **Save As** dialog box appears,
which allows you to enter a file name to save as.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Save**
\> **Save with Encoding** \> **Save as System Default**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_SAVE_ANSI (4102)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4102);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4102
```
