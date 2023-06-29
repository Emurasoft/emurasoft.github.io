# Logical Home or Start of Text command

### Summary

> Moves the cursor to the start of the current logical line or the start of text.

### Description

> Moves the cursor to either the start of the current logical line, or the first
> non-white space character of the current line. If the cursor is within white
> space characters at the beginning of the line, this command moves the cursor
> to the first non-white space character of the line.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Logical Home or Start of**
**Text**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_LOGICAL\_HOME\_TEXT (4333)

### Macros

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineLogical \| eeLineHomeText);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineLogical Or eeLineHomeText