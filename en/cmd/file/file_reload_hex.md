# Reload as Binary (Hex View)

### Summary

> Reloads the current file using Binary (Hex View) encoding.

### Description

> This command reloads the current file from the disk using the Binary (Hex View)
> encoding. If the document is changed within EmEditor, the prompt message
> "Are you sure you want to abandon changes?" appears. Selecting **Yes**
> will discard the changes without saving, and will reload the new contents.
> Selecting **No** will abort reloading and will allow you to continue
> editing the document.

### How to Run

- Default Menu: **File** \> **Reload** \> **Binary (Hex View)**
- [All Commands](../tools/all_commands): **File** \> **Reload**
\> **Binary (Hex View)**
- Toolbar: ![](../../images/reload.gif) (on
the arrow) > **System Default**
- Status Bar: (double-click on **Encodings**) \> **Binary (Hex View)**
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_FILE\_RELOAD\_HEX (4439)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4439);

#### \[VBScript\]

> editor.ExecuteCommandByID 4439
