# Fonts List command

### Summary

> Selects a recently used font (multiple items).

### Description

> This command consists of multiple menu items, displaying a list of recently
> used fonts. This command selects the specified font. The number of fonts to
> be displayed as the recent files can be set on the
> **Number**
> **of Recent Fonts** text box on the
> [**History** page](../../dlg/customize/history/index) of
> the [**Customize** dialog box](../../dlg/customize/index),
> under the **Tools** Menu ( **Tools** \> **Customize** \> **History**).

### How to Run

- Default Menu: **View** \> ( **Recent Font**)
- [All Commands](../tools/all_commands): **View** \> **Font** >
**Recent Font** \> ( **Recent Font**)
- Toolbar: ![](../../images/fontpopup.gif) (on
the arrow) >
( **Recent Font**)
- Status Bar: None
- Default Shortcut Key: None

### Plug-in Command ID

- From EEID\_MRU\_FONT1 through ID\_MRU\_FONT1 + 63 (from 4736 through 4736 +
63)

### Macros

#### \[JavaScript\]

> editor.ExecuteCommandByID(4736 + i); // i is an integer from 0 through 63

#### \[VBScript\]

> editor.ExecuteCommandByID 4736 + i   ' i is an integer from 0
> through 63