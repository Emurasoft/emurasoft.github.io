# Match Whole Word (Find toolbar) command

## Summary

Toggles the Match Whole Word button on the Find toolbar.

## Description

Toggles the Match Whole Word button on the Find toolbar. When this command is toggled, searching will return results only when the whole word at the matched location matches the search term.
(e.g., "searches" will not be returned as a match for "search")

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Search**
\> **Find Toolbar** \> **Search Only Word**
- Toolbar: ![](../../images/find_only_word.png) (Find toolbar)
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FINDBAR_ONLY_WORD (4576)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4576);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4576
```
