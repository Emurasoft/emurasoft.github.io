# Matching Tag Extend command

## Summary

Extends the selection to the corresponding tag.

## Description

When the cursor is placed at an opening/closing tag in an XML or XHTML document, this command will extend the selection to the corresponding closing/opening tag.

## How to Run

- Default Menu:Search \>Select Current Tag
- [All Commands](../tools/all_commands):Edit \>Extend Selection
\>Matching Tag Extend
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+.

## Plug-in Command ID

```
EEID_SHIFT_NEXT_TAG (4602)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4602);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4602
```
