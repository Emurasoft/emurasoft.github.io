# Word Right Extend command

### Summary

> Extends the selection one word to the right.

### Description

> Extends the selection one word to the right. If there are white space
> characters
> after the word, this command extends the selection to the start of the next word.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Word Right Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+RIGHT ARROW

### Plug-in Command ID

- EEID\_SHIFT\_RIGHT\_WORD (4174)

### Macros

#### \[JavaScript\]

> document.selection.WordRight(true,1);

#### \[VBScript\]

> document.selection.WordRight true,1
