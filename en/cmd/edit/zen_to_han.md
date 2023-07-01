# Half-Width command

### Summary

> Converts all selected full-width characters to half-width characters.

### Description

> Converts all selected full-width characters to half-width characters.
> Full-width characters are typically included in Eastern Asian language
> fonts.

### How to Run

- Default Menu: **Convert** \> **Half-Width**
- [All Commands](../tools/all_commands): **Convert** \> **Half-Width**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- EEID\_ZEN\_TO\_HAN (4151)

### Macros

#### \[JavaScript\]

> document.selection.ChangeWidth(eeWidthHalfWidth \| eeWidthAllTypes);

#### \[VBScript\]

> document.selection.ChangeWidth eeWidthHalfWidth Or eeWidthAllTypes
