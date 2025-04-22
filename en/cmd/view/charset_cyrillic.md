# Display in Cyrillic font command

## Summary

Displays text in a Cyrillic font.

## Description

Selects the Cyrillic font from the font category. The fonts in each font
category can be set on the [**Customize Font** dialog box](../../dlg/properties/font/index).
Changing the font category will not change the encoding to use to open a
file. If you want to change the encoding and reload the file, select the
[**Reload with Encoding** (multiple menu) command](../file/file_reload_defined).

## How to Run

- Default Menu: **View** \> **Font Category** > **Cyrillic**
- [All Commands](../tools/all_commands): **View** \> **Font** >
**Font Category** > **Cyrillic**
- Toolbar: ![](../../images/fontpopup.png)
(on the arrow) > **Font Category** \> **Cyrillic**
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_CHARSET_CYRILLIC (8710)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(8710);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 8710
```
