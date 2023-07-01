# Full-Width command

### Summary

> Converts all selected half-width characters to full-width characters.

### Description

> Converts all selected half-width characters to full-width characters.
> Full-width characters are typically included in Eastern Asian language
> fonts.

### How to Run

- Default Menu: **Convert** \> **Full-Width**
- [All Commands](../tools/all_commands): **Convert** \> **Full-Width**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_HAN\_TO\_ZEN (4152)

### Macros

#### \[JavaScript\]

> document.selection.ChangeWidth(eeWidthFullWidth \| eeWidthAllTypes);

#### \[VBScript\]

> document.selection.ChangeWidth eeWidthFullWidth Or eeWidthAllTypes
