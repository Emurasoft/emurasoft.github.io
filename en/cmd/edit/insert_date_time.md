# Date and Time command

### Summary

> Inserts the current date and time.

### Description

> Inserts the current date and time at the cursor position. This commands
> inserts the date followed by a space and then by the time. The formats used
> for the time and date can be configured in Windows by selecting the **Regional & Language Options** in **Control Panel**, then selecting **Date & Time**.

### How to Run

- Default Menu: **Insert** \> **Date and Time**
- [All Commands](../tools/all_commands): **Insert** \> **Date and Time**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: SHIFT+F5

### Plug-in Command ID

- EEID\_INSERT\_DATE\_TIME (4138)

### Macros

#### \[JavaScript\]

> document.selection.InsertDate(eeDateDateTime);

#### \[VBScript\]

> document.selection.InsertDate eeDateDateTime
