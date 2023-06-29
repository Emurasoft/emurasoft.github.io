# Home or Start of Text command

### Summary

> Moves the cursor to the first non-white space character of the current
> line.

### Description

> Moves the cursor to the start of the current line. This command ignores any white space
> at the beginning of the current line, and places the cursor next to the
> first non-white space character.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
>  **Home or Start of Text**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: HOME

### Plug-in Command ID

- EEID\_HOME\_TEXT (4296)

### Macros

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineView \| eeLineHomeText);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineView \| eeLineHomeText