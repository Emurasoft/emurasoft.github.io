# Find Matching Tag command

### Summary

> Moves the cursor to the corresponding tag.

### Description

> When the cursor is placed at a tag in an XML or XHTML document, this command will
> move the cursor to the corresponding tag. If the cursor is outside of the area bounded by the tags, it will be placed outside at the corresponding tag. If it is inside of the area about by the
> tags, it will be placed inside at the corresponding tag.

### How to Run

- Default Menu: **Search** \> **Find Matching Tag**
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Find Matching Tag**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+.

### Plug-in Command ID

- EEID\_NEXT\_TAG (4601)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4601);

#### \[VBScript\]

> editor.ExecuteCommandByID 4601
