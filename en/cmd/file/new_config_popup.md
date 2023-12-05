# New (popup menu) command

## Summary

Shows a popup menu to create a new file with a specified
configuration.

## Description

This command displays a new EmEditor window and prepares to start writing a
new document. This command will not create a file on disk immediately. The
file will not be created until you select the [**Save** command](file_save) or the [**Save As** command](file_save_as) after you
write something.

This command displays a popup menu, and allows you to select a
configuration to begin with (such as Text, HTML, VBScript, etc). If the specified configuration is configured with a template file,
the template will be used as the starting document. A template file, encoding for a new file,
the newline characters, and the font category can be set in
the [**New File** **Details** dialog box](../../dlg/properties/file/new_details/index), which can be accessed by clicking the
[**Properties for Current Configuration** button](../tools/customize) (or press ALT + ENTER), selecting the
[**File** page](../../dlg/properties/file/index), and then
clicking the **New**
**Files**
button.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **New** \> **New (Popup Menu)**
- Toolbar: ![](../../images/filenew.gif) (on
the arrow)
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_NEW_CONFIG_POPUP (4281)
```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4281);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4281
```
