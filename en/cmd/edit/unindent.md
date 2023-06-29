# Decrease Line Indent command

### Summary

> Decreases line indent at the selected area.

### Description

> Decreases line indent by removing one tab character at the beginning of each line
> at the selected area. If multiple lines are selected, this command is equivalent
> to the [**Tab Left or Decrease Line Indent** command](shift_tab).

### How to Run

- Default Menu: **Convert** \> **Decrease Line Indent**
- [All Commands](../tools/all_commands): **Convert** \> **Decrease Line Indent**
- Toolbar: ![](../../images/unindent.gif)
- Status Bar: None
- Default Keyboard Shortcut: SHIFT + TAB

### Plug-in Command ID

- EEID\_UNINDENT (4359)

### Macros

#### \[JavaScript\]

> document.selection.UnIndent();

#### \[VBScript\]

> document.selection.UnIndent