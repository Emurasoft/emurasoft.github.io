# Discard Diff command

## Summary

Discards the edits of Fast View mode and deletes the diff file.

## Description

This command is available in Fast View mode when the document has edits or the diff file of the current file exists. After you confirm, EmEditor discards the edits of the document, including the edits saved in the diff file, and deletes the diff file. The original file is not changed.

To delete the diff files of files that are not open, use the [**Fast View** page](../../dlg/customize/fast_view/index) of the **Customize** dialog box. See [To Open and Edit Huge Files in Fast View Mode](../../howto/file/file_fast_view) for details.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Diff** \> **Discard Diff**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_FAST_VIEW_DISCARD_DIFF (23293)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(23293);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 23293
```
