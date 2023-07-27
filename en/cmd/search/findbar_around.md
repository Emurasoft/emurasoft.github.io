# Wrap Around (Find toolbar) command

## Summary

Toggles the Wrap Around button on the Find toolbar.

## Description

Toggles the Wrap Around button on the Find toolbar. When this command is toggled, EmEditor will move to the beginning or end of the document to continue searching when the end
or beginning of the document is reached during aFind Next orFind Previous command.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Search
\>Find Toolbar \>Wrap Around
- Toolbar: ![](../../images/find_around.png) (Find toolbar)
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_FINDBAR_AROUND (4577)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4577);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4577
```
