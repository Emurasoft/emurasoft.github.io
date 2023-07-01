# Reload as Same Encoding command

### Summary

> Reloads the file using the default encoding.

### Description

> This command reloads the current file from the disk. If changes exist
> on the file since the last reloaded or opened period, this command will replace the
> document with the latest contents. If the document was changed, the prompt message "Are you sure you want to abandon changes?"
> appears. Selecting **Yes** will discard the changes without saving, and
> will reload the new contents. Selecting **No** will abort reloading and
> will allow you to continue editing the document.

### How to Run

- Default Menu: **File** \> **Reload** \> **Same Encoding**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **Same Encoding**
- Toolbar: ![](../../images/reload.gif) (not
on the arrow)
- Status Bar: None
- Default Shortcut Key: None

### Plug-ins command ID

- EEID\_FILE\_RELOAD (4109)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4109);

#### \[VBScript\]

> editor.ExecuteCommandByID 4109
