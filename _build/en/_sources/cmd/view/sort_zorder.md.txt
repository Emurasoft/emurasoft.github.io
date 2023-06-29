# Arrange by Active command

### Summary

> Arranges tabs by active order.

### Description

> Arranges tabs by most recently active (most recently active appears to the left). If the [**Auto Arrange** command](auto_sort) is checked, this command is called each time when a file is opened or a document is activated, and automatically arranged. If the
> [**Auto Arrange** command](auto_sort) is not checked, this command is called once.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **View** \> **Arrange Tabs by**
\> **Active**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_SORT\_ZORDER (4401)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4401);

#### \[VBScript\]

> editor.ExecuteCommandByID 4401