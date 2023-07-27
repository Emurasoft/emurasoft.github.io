# Toggle Vertical Split command

## Summary

Toggles the vertical window split.

## Description

If the current window is split horizontally or not split at all, this command
will split the current window into vertical panes, and will fix the split position
at the center of the window immediately. If the current window is already
split vertically, this command will remove the vertical split from the
current window.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Window
\>Split \>Toggle Vertical Split
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_WINDOW_SPLIT_VERT_TOGGLE (4386)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4386);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4386
```
