# Matching Parenthesis/Bracket Extend command

## Summary

Extends the selection to the corresponding parenthesis/bracket.

## Description

When the cursor is placed at an opening/closing parenthesis or bracket, this
command will extend the selection to the corresponding closing/opening bracket.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Extend Selection**
\> **Matching Parenthesis/Bracket**
**Extend**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+SHIFT+\]

## Plug-in Command ID

```
EEID_SHIFT_NEXT_PAREN (4277)```

## Macros

### \[JavaScript\]

```
document.selection.GoToBrace(true);
```

### \[VBScript\]

```
document.selection.GoToBrace true
```
