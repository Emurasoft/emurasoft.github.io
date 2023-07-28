# Paste in Quotes command

## Summary

Inserts the contents of the Clipboard with quotes.

## Description

Pastes the Clipboard contents with the quote marks at the cursor position. Before this command, use the
[**Copy** command](edit_copy) or the
[**Cut** command](edit_cut) to put text on the Clipboard.
This command uses the [**system default encoding**](../../glossary/systemdefaultencoding) if the
**Always Paste as ANSI** check box on the [**General** page](../../dlg/properties/general/index) of the Properties dialog box is checked, or Unicode if not checked.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Paste**
\> **Paste in Quotes**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+B

## Plug-in Command ID

```
EEID_PASTE_PREFIX (4132)```

## Macros

### \[JavaScript\]

```
document.selection.Paste(eeCopyQuotes);
```

### \[VBScript\]

```
document.selection.Paste eeCopyQuotes
```
