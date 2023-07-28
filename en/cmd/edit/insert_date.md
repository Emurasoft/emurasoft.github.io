# Time and Date command

## Summary

Inserts the current time and date.

## Description

Inserts the current time and date at the cursor position. This commands
inserts the time followed by a space and then by the date. The formats used
for the time and date can be configured in Windows by selecting the **Regional & Language Options** in **Control Panel**, then selecting **Date & Time**.

## How to Run

- Default Menu: **Insert** \> **Time and Date**
- [All Commands](../tools/all_commands): **Insert** \> **Time and Date**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_INSERT_DATE (4137)```

## Macros

## \[JavaScript\]

```
document.selection.InsertDate(eeDateTimeDate);
```

## \[VBScript\]

```
document.selection.InsertDate eeDateTimeDate
```
