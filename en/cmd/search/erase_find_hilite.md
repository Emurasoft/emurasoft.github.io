# Erase Find Highlight command

## Summary

Erases highlights from search terms.

## Description

Erases all highlights for previously run search strings present on the current
document.

## How to Run

- Default Menu: **Search** \> **Erase Find Highlight**
- [All Commands](../tools/all_commands): **Search**
\> **Erase Find Highlight**
- Toolbar:
![](../../images/erasefindhilite.png)
- Status Bar: None
- Default Shortcut Key: ALT+F3

## Plug-in Command ID

```
EEID_ERASE_FIND_HILITE (4206)
```

## Macros

### \[JavaScript\]

```
document.HighlightFind=false;
```

### \[VBScript\]

```
document.HighlightFind=false
```
