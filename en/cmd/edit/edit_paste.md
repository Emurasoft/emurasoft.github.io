# Paste command

## Summary

Inserts the contents of the Clipboard at the cursor position.

## Description

Inserts the contents of the Clipboard at the cursor position. Before this command, use the
[**Copy** command](edit_copy) or the
[**Cut** command](edit_cut) to put text on the Clipboard.
This command uses the [**system default encoding**](../../glossary/systemdefaultencoding) if the
**Always Paste as ANSI** check box
is checked on the [**General** page](../../dlg/properties/general/index) of the Properties dialog box, or Unicode if not checked.

## How to Run

- Default Menu: **Edit** \> **Paste**
- [All Commands](../tools/all_commands): **Edit** \> **Paste**
\> **Paste**
- Toolbar: ![](../../images/paste.png)
- Status Bar: None
- Default Keyboard Shortcut: CTRL+V or Shift+Insert

## Plug-in Command ID

```
EEID_EDIT_PASTE (4129)
```

## Macros

### \[JavaScript\]

```
document.selection.Paste(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.Paste eeCopyUnicode
```
