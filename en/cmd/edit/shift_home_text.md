# Home or Start of Text Extend command

### Summary

> Extends the selection to the start of the current line or the start of the
> text on that line.

### Description

> Selects all text between the cursor position and the first non-white space
> character at the beginning of the current line.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Home or Start of Text Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+HOME

### Plug-in Command ID

- EEID\_SHIFT\_HOME\_TEXT (4297)

### Macros

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineView \| eeLineHomeText);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineView Or eeLineHomeText