# Copy command

## Summary

Copies the selection or the current line and pastes it to the Clipboard.

## Description

Copies the selected text and moves it to the Clipboard. After this command, you can place the selection by moving the cursor to a different location running the [**Paste** command](edit_paste).

## How to Run

- Default Menu: **Edit** \> **Copy**
- [All Commands](../tools/all_commands): **Edit** \> **Copy**
\> **Copy**
- Toolbar: ![](../../images/copy.png)
- Status Bar: None
- Default Keyboard Shortcut: CTRL+C or CTRL+INSERT

## Plug-in Command ID

```
EEID_EDIT_COPY (4127)
```

## Macros

### \[JavaScript\]

```
document.selection.Copy(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.Copy eeCopyUnicode
```
