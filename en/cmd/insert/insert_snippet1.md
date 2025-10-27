# Insert Snippet command

## Summary

Inserts a specified snippet at the current cursor position (multiple items).

## Description

This command consists of multiple menu items, allowing you choose a snippet to insert at the cursor position.

## How to Run

- Default Menu: **Insert** \> **(Insert Snippet)**
- [All Commands](../tools/all_commands): **Insert** \> **Snippets** \> **(Insert Snippet)**
- Toolbar: None
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_INSERT_SNIPPET1 through EEID_INSERT_SNIPPET1 + 1023 (from 30208 through 30208 + 1023)
```

## Macros

## \[JavaScript\]

```
editor.ExecuteCommandByID(30208 + i); // i is an integer from 0 through 1023
```

## \[VBScript\]

```
editor.ExecuteCommandByID 30208 + i   ' i is an integer from 0 through 1023
```
