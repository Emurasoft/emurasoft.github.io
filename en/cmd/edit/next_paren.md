# Find Matching Parenthesis/Bracket command

## Summary

Moves the cursor to the corresponding parenthesis/bracket.

## Description

When the cursor is placed at a parenthesis or bracket, this command will
move the cursor to the corresponding parenthesis or bracket. If the cursor is outside of the area bounded by the parentheses or brackets, it will be placed outside at the corresponding
parenthesis/bracket. If it is inside of the area about by the parentheses/brackets, it will be placed inside at the corresponding parenthesis/bracket.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Move Cursor Horizontally**
\> **Find Matching**
**Parenthesis/Bracket**
- Toolbar: ![](../../images/nextparen.png)
- Status Bar: None
- Default Keyboard Shortcut: CTRL+\]

## Plug-in Command ID

```
EEID_NEXT_PAREN (4276)
```

## Macros

### \[JavaScript\]

```
document.selection.GoToBrace(false);
```

### \[VBScript\]

```
document.selection.GoToBrace false
```
