# Next Bookmark in This Group command

## Summary

Goes to the next bookmark in this group.

## Description

Moves the cursor to the next bookmark in this group. If no bookmark exists on
the current document, this command will go to the first bookmark in the next
document. If only one document contains bookmarks, it will go straight to
the first bookmark of that document.

## How to Run

- Default Menu: **Bookmarks** \> **This Group** \> **Next Bookmark**
- [All Commands](../tools/all_commands): **Bookmarks** \> **This Group** \> **Next Bookmark**
- Toolbar: ![](../../images/bookmarknext.png)
- Status Bar: None
- Default Keyboard Shortcut: F2

## Plug-in Command ID

```
EEID_BOOKMARK_NEXT (4321)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4321);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4321
```
