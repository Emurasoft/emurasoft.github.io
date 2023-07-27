# Toggle Horizontal Split command

## Summary

Toggles the horizontal window split.

## Description

If the current window is split vertically or not split at all, this command
will split the current window into horizontal panes, and will fix the split position
at the center of the window immediately. If the current window is already
split horizontally, this command will remove the horizontal split from the
current window.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands):Window
\>Split \>Toggle Horizontal Split
- Toolbar: ![](../../images/windowsplithorzfix.gif)
- Status Bar: None
- Default Shortcut Key: CTRL + -

## Plug-in Command ID

```
EEID_WINDOW_SPLIT_HORZ_TOGGLE (4385)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4385);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4385
```
