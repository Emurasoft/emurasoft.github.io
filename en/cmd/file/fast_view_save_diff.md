# Save Diff command

## Summary

Saves the edits of Fast View mode and the positions of the lines to a diff file in the EmEditor data folder, without rewriting the file, so that the file opens faster.

## Description

This command is available in Fast View mode. It saves your edits to a diff file without rewriting the original file, which can take a long time for a huge file. The next time you open the file, the edits are applied automatically. To write the edits into the file, save the document with **Save and merge now** of the [**Save** command](file_save).

The diff file also stores the positions of the lines of the file, so that the file opens without finding the positions of the lines again. If the document has no edits, only the positions of the lines are saved.

Diff files are saved in the **FastView** folder in the local application data folder of EmEditor. You can see and delete them on the [**Fast View** page](../../dlg/customize/fast_view/index) of the **Customize** dialog box. See [To Open and Edit Huge Files in Fast View Mode](../../howto/file/file_fast_view) for details.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Diff** \> **Save Diff**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_FAST_VIEW_SAVE_DIFF (23291)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(23291);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 23291
```
