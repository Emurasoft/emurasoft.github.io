# Toggle Bookmark command

## Summary

Toggles a bookmark on the current line.

## Description

Sets a bookmark on the current line if not already set, or resets the bookmark if
set.

## How to Run

- Default Menu: **Bookmarks** \> **Toggle Bookmark**
- [All Commands](../tools/all_commands): **Bookmarks** \> **Toggle Bookmark**
- Toolbar: ![](../../images/bookmarktoggle.gif)
- Status Bar: None
- Default Keyboard Shortcut: CTRL+F2

## Plug-in Command ID

```
EEID_BOOKMARK_TOGGLE (4320)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4320);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4320
```
