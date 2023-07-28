# Find Previous Warning Character/Unicode command

## Summary

Finds the previous warning or Unicode character that cannot be converted to the encoding for saving.

## Description

Finds the previous Unicode character that cannot be converted to the encoding for
saving, by selecting the character. If the Unicode character which cannot
be converted is not highlighted, this command
will highlight it. The highlight color will be the color specified by
**Highlight (8)** under the
**Specify Part** list box on the
[**Display** page](../../dlg/properties/display/index) of
the Current Configuration Properties dialog box.

The encoding used to save the file will be determined as follows:

If the prompt
message "This document contains characters in Unicode format which will
be lost if you save this document as the selected encoding for saving. To
keep the Unicode information, click Cancel below, select Save As, and then
select one of the Unicode options from the Encoding drop-down list box.
"Continue?" appears, the file will
be saved using the encoding you specified when trying to save the file.

After you select the [**Erase Unicode Highlight** command](erase_unicode_hilite), the encoding used to save the
file will be the encoding displayed in the status bar.

## How to Run

- Default Menu: **Search** \> **Find Previous Warning Character/Unicode**
- [All Commands](../tools/all_commands): **Search** \> **Unicode** \> **Find Previous Warning Character/Unicode**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: SHIFT+F9

## Plug-in Command ID

```
EEID_FIND_PREV_UNICODE (4376)```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(4376);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4376
```
