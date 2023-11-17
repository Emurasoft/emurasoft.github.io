# Copy and Deselect command

## Summary

Copies the selection, pastes it to the Clipboard and deselects the text.

## Description

Copies the selected text to the Clipboard, and deselect any selected text.
This command is equivalent to the [**Copy** command](edit_copy) followed by the [**Cancel** command](escape). After this command, you
can place the selection by moving the cursor to a different location
and running the [**Paste** command](edit_paste).

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Copy**
> **Copy and Deselect**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_EDIT_COPY_DESELECT (4128)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4128);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4128
```
