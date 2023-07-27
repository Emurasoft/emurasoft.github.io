# Paste In Quotes And Newline Characters command

## Summary

Inserts the Clipboard contents in quotes and with newline characters.

## Description

Pastes the contents of the Clipboard with quote marks and inserts a newline character at the cursor
position. Before this command, use the
[Copy command](edit_copy) or the
[Cut command](edit_cut) to put text on the Clipboard.
This command uses the [system default encoding](../../glossary/systemdefaultencoding) if the
Always Paste as ANSI check box
on the [General page](../../dlg/properties/general/index) of the Properties dialog box is checked, or Unicode if not checked.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Edit \>Paste
\>Paste In Quotes And Newline Characters
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_PASTE_PREFIX_RETURN (4134)```

## Macros

### \[JavaScript\]

```
document.selection.Paste(eeCopyQuotes \| eeCopyNL);
```

### \[VBScript\]

```
document.selection.Paste eeCopyQuotes Or eeCopyNL
```
