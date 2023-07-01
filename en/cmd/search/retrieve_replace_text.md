# Set Word to Replace command

### Summary

> Sets the current word as the replace string.

### Description

> Sets the word at the cursor position to the replace string for the [**Replace Next** command](replace_next).  After running this command, if you
> select the [**Replace Next** command](replace_next), it will
> immediately replace the next query word with the word specified with this command. If the
> Custom is selected for the **\> button**, the [**Replace** dialog box](../../dlg/replace/index)
> will display the word specified by this command as default.

### How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Search**
\> **Set Word to Replace**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- EEID\_RETRIEVE\_REPLACE\_TEXT (4446)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4446);

#### \[VBScript\]

> editor.ExecuteCommandByID 4446
