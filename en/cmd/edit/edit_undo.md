# Undo command

## Summary

Undo the last action.

## Description

Undo the last action. If you repeat this command, you can undo several
previous consecutive
actions. If the
**Undo**
**Character by Character** check box is
checked on the [**Edit** page](../../dlg/customize/edit/index) of the [**Customize** dialog box](../../dlg/customize/index), a string insert will be undone character by character.

## How to Run

- Default Menu: **Edit** \> **Undo**
- [All Commands](../tools/all_commands): **Edit** \> **Undo**
- Toolbar: ![](../../images/editundo.png)
- Status Bar: None
- Default Keyboard Shortcut: CTRL+Z or ALT+BACKSPACE

## Plug-in Command ID

```
EEID_EDIT_UNDO (4124)
```

## Macros

### \[JavaScript\]

```
document.Undo();
```

### \[VBScript\]

```
document.Undo
```
