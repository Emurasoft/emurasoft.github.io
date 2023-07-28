# Untabify All command

## Summary

Converts tabs to equivalent spaces throughout the entire document.

## Description

Converts tabs at the start of all lines throughout the entire document into
spaces. The number of spaces for a
tab can be set in the [**Tab/Indent** dialog box](../../dlg/properties/general/indent/index). This is equivalent to the
[**Untabify** command](untabify) after selecting the
entire document, but this command does not extend the selection.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Advanced** \> **Untabify Document**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_TAB_TO_SPACE (4253)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4253);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4253
```
