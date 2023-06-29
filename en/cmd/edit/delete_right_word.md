# Delete Right Word command

### Summary

> Deletes the word to the right of the cursor.

### Description

> Deletes text from the cursor position to the first character of the next
> word in the current line.
> This command does delete white space.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Delete**
\> **Delete Right Word**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+DELETE

### Plug-in Command ID

- EEID\_DELETE\_RIGHT\_WORD (4275)

### Macros

#### \[JavaScript\]

> document.selection.WordRight(true,1);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.WordRight true,1
>
> document.selection.Delete 1