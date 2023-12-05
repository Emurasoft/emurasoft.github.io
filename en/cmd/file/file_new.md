# New Text command

## Summary

Creates a new text file.

## Description

This command displays a new EmEditor window and prepares to start writing a
new document. This command will not immediately create a file on disk. The
file will not be created until you select the [**Save** command](file_save) or the [**Save As** command](file_save_as) after you write something.

By default, this command uses the Text configuration. You can change the
default configuration at the
[**Define Configurations** dialog box](../../dlg/configurations/index). By default, the Text
configuration uses the [system default encoding](../../glossary/index), CR+LF  (Windows) as the newline characters,
usually Western European as the font category on the English version of
Windows, and does not use a template. You can change the default settings in
the [**New File** **Details** dialog box](../../dlg/properties/file/new_details/index), which can be accessed by clicking the
[**Properties for Current Configuration** button](../tools/customize) (or press ALT + ENTER), selecting the
[**File** page](../../dlg/properties/file/index), and then
clicking the **New**
**Files**
button.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **File** \> **New** \> **New Text**
- Toolbar: ![](../../images/filenew.gif) (not
on the arrow)
- Status Bar: None
- Default Shortcut Key: CTRL+N

## Plug-in Command ID

```
EEID_FILE_NEW (4096)
```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4096);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4096
```
