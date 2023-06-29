# Spelling Suggestion command

### Summary

> Selects this suggestion for the correct spelling (multiple items).

### Description

> Selects this suggestion for the correct spelling, and replaces the misspelled word with the selected suggestion (not document-wide).

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Edit** \> **Spelling** \> **(Spelling Suggestions)**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- From EEID\_SPELL\_SUGGEST through EEID\_SPELL\_SUGGEST + 31 (from 8768 through 8768 + 31)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(8768 + i);  // i is an integer from 0 through 31

#### \[VBScript\]

> editor.ExecuteCommandByID 8768 + i  ' i is an integer from 0 through 31