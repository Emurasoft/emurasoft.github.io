# Select Word command

## Summary

Selects the word right of the current cursor position.

## Description

Selects the word right of the current cursor position. This command selects
all text characters between two white space characters.  White space is
only selected if the cursor is placed before the white space.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Select Word**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: ALT+F8

## Plug-in Command ID

```
EEID_SELECT_WORD (4251)```

## Macros

### \[JavaScript\]

```
document.selection.SelectWord();
```

### \[VBScript\]

```
document.selection.SelectWord
```
