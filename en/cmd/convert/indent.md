# Increase Line Indent command

## Summary

Increases the line indent in the selection.

## Description

Inserts a tab character at the beginning of each line at the selected area. If
multiple lines are selected, this command is equivalent to the
[**Tab or Increase Line Indent** command](../edit/tab).

## How to Run

- Default Menu: **Convert** \> **Increase Line Indent**
- [All Commands](../tools/all_commands): **Convert** \> **Increase Line Indent**
- Toolbar: ![](../../images/indent.png)
- Status Bar: None
- Default Keyboard Shortcut: None

## Plug-in Command ID

```
EEID_INDENT (4358)
```

## Macros

### \[JavaScript\]

```
document.selection.Indent();
```

### \[VBScript\]

```
document.selection.Indent
```
