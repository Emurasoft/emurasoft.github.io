# Find Previous Word command

### Summary

> Finds the previous occurrence of the specified text.

### Description

> Finds the previous occurrence of the specified string, if a string is
> selected. Otherwise, finds the previous occurrence of the word at the cursor
> position.

### How to Run

- Default Menu: **Search** \> **Find Previous Word**
- [All Commands](../tools/all_commands): **Search**
\> **Find Previous Word**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: CTRL+SHIFT+F3

### Plug-in Command ID

- EEID\_FIND\_PREV\_WORD (4205)

### Macros

#### \[JavaScript\]

> document.selection.FindRepeat(eeFindRepeatPrevious \| eeFindRepeatWord);

#### \[VBScript\]

> document.selection.FindRepeat eeFindRepeatPrevious Or eeFindRepeatWord