# Reload as UTF-16LE command

### Summary

> Reloads the current file using Unicode (UTF-16LE) encoding.

### Description

> This command reloads the current file from the disk using Unicode (UTF-16LE) encoding. If the document is changed within EmEditor, the prompt message
> "Are you sure you want to abandon changes?" appears. Selecting **Yes**
> will abandon the changes without saving, and will reload the new contents.
> Selecting **No** will abort reloading and will allow you to continue
> editing the document.

### How to Run

- Default Menu: **File** \> **Reload** \> **UTF-16LE**
- [All Commands](../tools/all_commands): **File** \> **Reload UTF-16LE**
- Toolbar: ![](../../images/reload.gif) (on
the arrow) > **UTF-16LE**
- Status Bar: (double-click on the **Encoding**) \> **UTF-16LE**
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_FILE\_RELOAD\_UNICODE (4257)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4257);

#### \[VBScript\]

> editor.ExecuteCommandByID 4257
