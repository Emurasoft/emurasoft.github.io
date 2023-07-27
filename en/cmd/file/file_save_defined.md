# List of Encodings to Save command

## Summary

Saves the current file using a specified encoding (multiple items).

## Description

This command consists of multiple menu items, from which you can select predefined
encodings. If the document is titled, this command saves the current file using the specified encoding. If  the document is untitled, theSave As dialog box appears, which allows you to enter a file name to save the file as.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):File \>Save
\>Save with Encoding \>(choose encoding)
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-ins command ID

- From EEID\_FILE\_SAVE\_DEFINED through ID\_FILE\_SAVE\_DEFINED + 255 (from 7680
through 7680 + 255)

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(7680 + i);  // i is an integer from 0
through 255
```

### \[VBScript\]

```
editor.ExecuteCommandByID 7680  + i  ' i is an integer from 0
through 255
```
