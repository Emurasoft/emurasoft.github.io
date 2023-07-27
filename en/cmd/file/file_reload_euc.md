# Reload as Japanese EUC command

## Summary

Reloads the current file using Japanese EUC encoding.

## Description

This command reloads the current file from the disk using the Japanese EUC
encoding. If the document is changed within EmEditor, the prompt message
"Are you sure you want to abandon changes?" appears. SelectingYes
will discard the changes without saving, and will reload the new contents.
SelectingNo will abort reloading and will allow you to continue
editing the document.

This command remains for compatibility with the older versions of
EmEditor. You can use the [Reload with\
Encoding (multiple menu) command](file_reload_defined) instead and specify Japanese EUC.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Reload
\>Japanese EUC
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FILE_RELOAD_EUC (4112)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4112);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4112
```
