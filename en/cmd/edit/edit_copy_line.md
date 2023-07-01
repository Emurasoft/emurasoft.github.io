# Copy Line(s) command

### Summary

> Copies the selected lines or current line and pastes it to the Clipboard.

### Description

> Copies the selected lines or one logical line of text at the cursor, and pastes it to the Clipboard. After
> this command, you can place the line(s) by moving the cursor to a
> different location and running the [**Paste** command](edit_paste).

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Copy**
\> **Copy Line(s)**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_EDIT\_COPY\_LINE (4192)

### Macros

#### \[JavaScript\]

> document.selection.SelectLine();
>
>
> document.selection.Copy(eeCopyUnicode);

#### \[VBScript\]

> document.selection.SelectLine
>
>
> document.selection.Copy eeCopyUnicode
