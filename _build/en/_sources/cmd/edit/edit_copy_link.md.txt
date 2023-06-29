# Copy Link command

### Summary

> Copies a hyperlink and pastes it to the Clipboard.

### Description

> Copies a hyperlink string at the cursor and pastes it to the Clipboard. After this
> command, you can place the selection by moving the cursor to a
> different location and running the [**Paste** command](edit_paste).

### How to Run

- Default Menu: **Edit** \> **Copy Link**
- [All Commands](../tools/all_commands): **Edit** \> **Copy**
\> **Copy Link**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_EDIT\_COPY\_LINK (4140)

### Macros

#### \[JavaScript\]

> document.selection.CopyLink();

#### \[VBScript\]

> document.selection.CopyLink