# Fast View command

## Summary

Toggles between the normal mode and Fast View mode for huge files.

## Description

Reopens the current document in Fast View mode, or in the normal mode if the document is already in Fast View mode. Fast View mode opens a huge file almost instantly without loading the whole file into memory, and allows you to view, search, and edit the file. See [To Open and Edit Huge Files in Fast View Mode](../../howto/file/file_fast_view) for details.

Files larger than the **Minimum file size to enable Fast View mode** on the [**Fast View** page](../../dlg/customize/fast_view/index) of the **Customize** dialog box are opened in Fast View mode automatically.

If the document has unsaved edits, EmEditor asks whether to save them before switching the mode. This command is not available for untitled documents.

## How to Run

- Default Menu: **Edit** \> **Fast View**
- [All Commands](../tools/all_commands): **Edit** \> **Advanced** \> **Fast View**
- Toolbar: None
- Status Bar: Double-click on **FAST**
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_FAST_VIEW (23289)
```

## Macros

### \[JavaScript\]

```
document.FastView = true;
or
document.FastView = false;
```

### \[VBScript\]

```
document.FastView = True
or
document.FastView = False
```
