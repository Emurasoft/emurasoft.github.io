# Dictionary command

### Summary

> Selects this dictionary to check spelling (multiple items).

### Description

> Selects this dictionary to check spelling. The EmEditor installer includes a U.S. English dictionary. Additional dictionaries are available for download at the **[OpenOffice.org wiki](https://wiki.openoffice.org/wiki/Dictionaries)**. To add a dictionary, copy **\*.dic** and **\*.aff** files
> into the **Dictionaries** sub folder of the EmEditor install folder (usually C:\\Program Files\\EmEditor\\Dictionaries).

### How to Run

- Default Menu: **Edit** \> **Spelling** \> **Dictionaries** \> **(Dictionaries)**
- [All Commands](../tools/all_commands): **Edit** \> **Spelling** \> **Dictionaries** \> **(Dictionaries)**
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: None

### Plug-in Command ID

- From EEID\_SELECT\_DICTIONARY through EEID\_SELECT\_DICTIONARY + 255 (from 22016 through 22016 + 255)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(22016 + i);  // i is an integer from 0 through 255

#### \[VBScript\]

> editor.ExecuteCommandByID 22016 + i  ' i is an integer from 0 through 255
