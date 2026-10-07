# Erase Unicode Highlight command

## Summary

Clears highlights marking Unicode characters that cannot be converted to the selected encoding.

## Description

Resets highlighting for searched Unicode characters that cannot be converted
to the encoding for saving. This command also resets the encoding for saving
that is set by the [**Find Next Unicode** command](find_next_unicode) or [**Find Previous Unicode** command](find_prev_unicode).

## How to Run

- Default Menu: **Search** \> **Erase Unicode Highlight**
- [All Commands](../tools/all_commands): **Search** \> **Unicode** \> **Erase Unicode Highlight**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: ALT+F9

## Plug-in Command ID

```
EEID_ERASE_UNICODE_HILITE (4377)```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4377);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4377
```
