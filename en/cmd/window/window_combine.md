# Enable Tabs command

### Summary

> Enables tabs to combine or disable tabs to separate all windows.

### Description

> Enables the tabs if disabled, or disables the tabs if already enabled. When the tabs are enabled, all currently open documents are displayed on a tab menu at the top of the window. Only one EmEditor
> icon will be displayed on the Windows Task Bar.

### How to Run

- Default Menu: **Window** \> **Enable Tabs**
- [All Commands](../tools/all_commands): **Window**
\> **Enable Tabs** \> **Enable Tabs**
- Toolbar: ![](../../images/windowcombine.gif)
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_WINDOW\_COMBINE (4342)

### Macros

#### \[JavaScript\]

> editor.EnableTab = !editor.EnableTab;

#### \[VBScript\]

> editor.EnableTab = Not editor.EnableTab
