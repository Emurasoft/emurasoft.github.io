# Compare command

## Summary

Compares the two most recently viewed documents without specifying options.

## Description

Compares the two most recently viewed documents without specifying options. EmEditor will prompt if the encodings of the two files are not the same, but will proceed with the comparison.

Documents in Fast View mode can also be compared, after all the lines of the documents are found. The [**Ignore Comments**](ignore_comment), [**Copy to Other**](copy_to_other), [**Copy All to Other**](copy_all_to_other), and [**Bookmark Changes**](compare_bookmark) commands are not available when a document is in Fast View mode.

## How to Run

- Default Menu: **Compare** \> **Compare Direct**
- [All Commands](../tools/all_commands): **Compare** \> **Compare Direct**
- Toolbar: ![](../../images/compare24x16.png)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_COMPARE_DIRECT (4492)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4492);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4492
```
