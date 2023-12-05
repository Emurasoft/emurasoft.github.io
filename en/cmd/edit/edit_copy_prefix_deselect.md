# Copy in Quotes and Deselect command

## Summary

Copies the selection in quotes, pastes it to the Clipboard and deselects
text.

## Description

Copies the selected text with the quote marks to the Clipboard, and
deselects the text.
This command is equivalent to the [**Copy Text in****Quotes** command](edit_copy) followed by the [**Cancel** command](escape). After this command, you
can place the selection by moving the cursor to a different location
and running the [**Paste** command](edit_paste).

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Copy**
\> **Copy in Quotes and Deselect**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+Q

## Plug-in Command ID

```
EEID_EDIT_COPY_PREFIX_DESELECT (4131)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID (4131);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4131
```
