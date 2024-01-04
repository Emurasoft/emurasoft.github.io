# Find Next Word command

## Summary

Finds the next occurrence of the current word.

## Description

Finds the next occurrence of the specified string, if a string is selected.
Otherwise, finds the next occurrence of the word at the cursor position.

## How to Run

- Default Menu: **Search** \> **Find Next Word**
- [All Commands](../tools/all_commands): **Search**
\> **Find Next Word**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: Ctrl+F3

## Plug-in Command ID

```
EEID_FIND_NEXT_WORD (4204)```

## Macros

### \[JavaScript\]

```
document.selection.FindRepeat(eeFindRepeatNext | eeFindRepeatWord);
```

### \[VBScript\]

```
document.selection.FindRepeat eeFindRepeatNext Or eeFindRepeatWord
```
