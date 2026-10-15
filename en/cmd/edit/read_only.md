# Read Only command

## Summary

Toggles read-only status for the current file.

## Description

Enables or disables the ability to save changes to the file.

In Fast View mode, turning on Read Only also turns off editing, and turning it off allows editing. If the document has unsaved edits, EmEditor asks whether to save them. See [To Open and Edit Huge Files in Fast View Mode](../../howto/file/file_fast_view) for details.

## How to Run

- Default Menu: **Edit** \> **Read Only**
- [All Commands](../tools/all_commands): **Edit** \> **Advanced**
\> **Read Only**
- Toolbar: None
- Status Bar: Double-click on **READ**
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_READ_ONLY (4113)```

## Macros

### \[JavaScript\]

```
document.ReadOnly=true;
or
document.ReadOnly=false;
```

### \[VBScript\]

```
document.ReadOnly=true
or
document.ReadOnly=false
```
