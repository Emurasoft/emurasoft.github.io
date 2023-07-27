# Display in OEM/DOS font command

## Summary

Displays text in a OEM/DOS font

## Description

Selects the OEM/DOS font from the font category. The fonts in each font
category can be set on the [Customize Font dialog box](../../dlg/properties/font/index).
Changing the font category will not change the encoding to use to open a
file. If you want to change the encoding and reload the file, select the
[Reload with Encoding (multiple menu) command](../file/file_reload_defined).

## How to Run

- Default Menu:View \>Font Category >OEM/DOS
- [All Commands](../tools/all_commands):View \>Font >
Font Category
\>OEM/DOS
- Toolbar: ![](../../images/fontpopup.gif)
(on the arrow) >Font Category \>OEM/DOS
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_CHARSET_OEM (8719)```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(8719);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 8719
```
