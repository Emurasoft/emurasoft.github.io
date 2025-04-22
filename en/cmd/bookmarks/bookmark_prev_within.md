# Previous Bookmark in This Document command

## Summary

Goes to the previous bookmark in this document.

## Description

Moves the cursor to the previous bookmark in the current document. If no bookmark exists on the current
document, this command will not move the cursor.

## How to Run

- Default Menu: **Bookmarks** \> **Previous Bookmark**
- [All Commands](../tools/all_commands): **Bookmarks** \> **Previous Bookmark**
- Toolbar: ![](../../images/bookmarkprevwithin.png)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_BOOKMARK_PREV_WITHIN (4352)
```

## Macros

### \[JavaScript\]

```
document.selection.PreviousBookmark();
```

### \[VBScript\]

```
document.selection.PreviousBookmark
```
