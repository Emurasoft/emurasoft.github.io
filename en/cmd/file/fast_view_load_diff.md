# Load Diff command

## Summary

Applies the edits saved in the diff file of the file in Fast View mode.

## Description

This command is available in Fast View mode when the diff file of the current file exists. It applies the edits saved with the [**Save Diff** command](fast_view_save_diff), or with **Save only my changes** of the [**Save** command](file_save), and turns off **Read Only**. If the document has unsaved edits, EmEditor asks whether to save them first.

The edits in the diff file are usually applied automatically when the file is opened. You can use this command to apply them again, for example, after you discarded unsaved edits.

The diff file cannot be applied if the file was changed after the diff file was saved, if the file is opened in a different encoding, or if the CSV setting that allows newlines in quoted cells is different. See [To Open and Edit Huge Files in Fast View Mode](../../howto/file/file_fast_view) for details.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Diff** \> **Load Diff**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_FAST_VIEW_LOAD_DIFF (23292)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(23292);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 23292
```
