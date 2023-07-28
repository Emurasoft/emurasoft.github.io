# Delete Word command

## Summary

Deletes the word at the current cursor position.

## Description

Deletes any text at the cursor position between two white space characters. This command deletes white space if there is no text present at the cursor position.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Delete**
\> **Delete Word**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+DELETE

## Plug-in Command ID

```
EEID_DELETE_WORD (4194)```

## Macros

### \[JavaScript\]

```
document.selection.SelectWord();
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.SelectWord
document.selection.Delete 1
```
