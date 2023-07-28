# Previous Document command

## Summary

Switches to the previous document.

## Description

Switches to the previous open EmEditor document. The behavior of this command depends on whether the
[**Switch to last used document for Next**\
**Document command** check box](../../dlg/customize/window/index) is checked. If it is checked, this command will switch to the earliest used document. If not checked, this command will switch to the previous document displayed on the
tab bar.

## How to Run

- Default Menu: **Window** \> **Previous Document**
- [All Commands](../tools/all_commands): **Window**
\> **Document Navigation** \> **Previous Document**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: CTRL+SHIFT+TAB

## Plug-in Command ID

```
EEID_PREV_WINDOW (4246)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4246);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4246
```
