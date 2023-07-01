# Copy in Quotes command

### Summary

> Copies the selection in quotes and pastes it to the Clipboard.

### Description

> Copies the selected text with the quote mark at the beginning of each line and put it on the Clipboard. After this command, you
> can place the selection by moving the cursor to a different location
> and running the [**Paste** command](edit_paste).

### How to Run

- Default Menu: **Edit** \> **Copy in Quotes**
- [All Commands](../tools/all_commands): **Edit** \> **Copy**
\> **Copy in Quotes**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_EDIT\_COPY\_PREFIX (4130)

### Macros

#### \[JavaScript\]

> document.selection.Copy(eeCopyQuotes);

#### \[VBScript\]

> document.selection.Copy eeCopyQuotes
