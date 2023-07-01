# Reload as UTF-16BE command

### Summary

> Reloads the current file using Unicode (UTF-16BE) encoding.

### Description

> This command reloads the current file from the disk using Unicode (UTF-16BE)
> encoding. If the document is changed within EmEditor, the prompt message
> "Are you sure you want to abandon changes?" appears. Selecting **Yes**
> will abandon the changes without saving, and will reload the new contents.
> Selecting **No** will abort reloading and will allow you to continue
> editing the document.

### How to Run

- Default Menu: **File** \> **Reload** \> **UTF-16BE**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **UTF-16BE**
- Toolbar: ![](../../images/reload.gif) (on
the arrow) > **UTF-16BE**
- Status Bar: (double-click on **Encodings**) \> **UTF-16BE**
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_FILE\_RELOAD\_UNICODE\_BIGENDIAN (4261)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4261);

#### \[VBScript\]

> editor.ExecuteCommandByID 4261
