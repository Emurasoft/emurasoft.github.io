# Next Bookmark in This Document command

## Summary

Goes to the next bookmark in this document.

## Description

Moves the cursor to the next bookmark in the current document. If no bookmark exists on the current
document, this command will not move the cursor.

## How to Run

- Default Menu: **Bookmarks** \> **Next Bookmark**
- [All Commands](../tools/all_commands): **Bookmarks** \> **Next Bookmark**
- Toolbar: ![](../../images/bookmarknextwithin.png)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_BOOKMARK_NEXT_WITHIN (4351)
```

## Macros

### \[JavaScript\]

```
document.selection.NextBookmark();
```

### \[VBScript\]

```
document.selection.NextBookmark
```
