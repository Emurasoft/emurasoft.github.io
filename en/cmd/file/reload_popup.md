# Reload (popup menu) command

### Summary

> Shows a popup menu to select an encoding to reload the file with.

### Description

> This command displays a popup menu, from which you can select an encoding
> to use for reloading. After an encoding is selected, this command reloads
> the file from the disk. If changes were made to the file since it was last reloaded
> or opened, this command will replace the document with the latest contents.
> If the document was changed within EmEditor, the prompt message "Are you sure
> you want to abandon changes?" appears. Selecting **Yes** will
> discard the
> changes without saving, and will reload the new contents. Selecting **No**
> will abort reloading and will allow you to continue editing the document.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **Popup Menu**
- Toolbar: ![](../../images/reload.gif) (on
the arrow)
- Status Bar: double-click on Encodings
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_RELOAD\_POPUP (4283)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4283);

#### \[VBScript\]

> editor.ExecuteCommandByID 4283
