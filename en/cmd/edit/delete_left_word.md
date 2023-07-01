# Delete Left Word command

### Summary

> Deletes the word to the left of the cursor.

### Description

> Deletes text from the cursor position to the first white space character
> encountered after the previous word in the current line.
> This command does not delete white space before a word.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Delete**
\> **Delete Left Word**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+BACKSPACE

### Plug-in Command ID

- EEID\_DELETE\_LEFT\_WORD (4280)

### Macros

#### \[JavaScript\]

> document.selection.WordLeft(true,1);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.WordLeft true,1
>
> document.selection.Delete 1
