# Paste as System Default Encoding command

## Summary

Pastes Clipboard contents using the [system default \
encoding](../../glossary/index).

## Description

Pastes the Clipboard contents at the cursor position using the
[**system default encoding**](../../glossary/systemdefaultencoding). Before this command, use the
[**Copy** command](edit_copy) or the
[**Cut** command](edit_cut) to put text on the Clipboard.
This command is equivalent to the [**Paste** \
command](edit_paste) if the
**Always Paste as ANSI** check box
is checked on the [**General** page](../../dlg/properties/general/index) of the Properties dialog box.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Paste**
\> **Paste as System Default Encoding**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: ALT+CTRL+V

## Plug-in Command ID

```
EEID_EDIT_PASTE_ANSI (4262)```

## Macros

### \[JavaScript\]

```
document.selection.Paste(eeCopySystemDefault);
```

### \[VBScript\]

```
document.selection.Paste eeCopySystemDefault
```
