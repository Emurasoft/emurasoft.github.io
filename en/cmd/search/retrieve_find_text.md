# Set Word to Find command

## Summary

Sets the current word as the query string.

## Description

Sets the word at the cursor position to the query string for the [**Find Next** command](edit_repeat).  After running this command, if you
select the [**Find Next** command](edit_repeat), it will
immediately find the next instances of the word specified with this command. If the
Word at Cursor is not checked in the menu displayed upon clicking the **\> button**, the [**Find** dialog box](../../dlg/find/index)
will display the word specified by this command as default.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Search**
\> **Set Word to Find**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_RETRIEVE_FIND_TEXT (4325)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4325);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4325
```
