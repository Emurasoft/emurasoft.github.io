# Reload as Binary (ASCII View)

### Summary

> Reloads the current file using Binary (ASCII View) encoding.

### Description

> This command reloads the current file from the disk using the Binary (ASCII View)
> encoding. If the document is changed within EmEditor, the prompt message
> "Are you sure you want to abandon changes?" appears. Selecting **Yes**
> will discard the changes without saving, and will reload the new contents.
> Selecting **No** will abort reloading and will allow you to continue
> editing the document.

### How to Run

- Default Menu: **File** \> **Reload** \> **Binary (ASCII View)**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **Binary (ASCII View)**
- Toolbar: ![](../../images/reload.gif) (on
the arrow) > **System Default**
- Status Bar: (double-click on **Encodings**) \> **Binary (ASCII View)**
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_FILE\_RELOAD\_BINARY (4438)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4438);

#### \[VBScript\]

> editor.ExecuteCommandByID 4438