# New Group Minimize command
## Summary

Detaches the current document from the combined window as a new group, and minimizes it.

## Description

Detaches the current document from combined windows as a new group, and minimizes. This is the same as dragging a tab outside of the current EmEditor window and selecting **New Group**
when prompted, then minimizing the new window.

## How to Run

- Default Menu: None
- [All Commands](../tools/all_commands): **Window** \>
**Group**
\> **New Minimized Group**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
EEID_NEW_GROUP_MINIMIZE (4392)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(4392);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4392
```
