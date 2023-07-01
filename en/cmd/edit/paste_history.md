# Cycle Clipboard Ring command

### Summary

> Inserts one of the contents from the Clipboard history at the cursor position.

### Description

> Inserts one of the contents from the Clipboard history (recently copied items) at the cursor position. Repeatedly selecting this command will cycle through the items in the Clipboard history.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Paste**
\> **Cycle Clipboard Ring**
- Toolbar: ![](../../images/cycle_clipboard_ring.gif)
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_PASTE\_HISTORY (4454)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4454);

#### \[VBScript\]

> editor.ExecuteCommandByID 4454
