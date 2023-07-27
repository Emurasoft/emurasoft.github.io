# Lowercase command

## Summary

Converts the selection to all lowercase letters.

## Description

Converts the selection to all lowercase letters. For instance, A will become a, Ä
will become ä, and Λ will become λ.

## How to Run

- Default Menu:Convert \>Lowercase
- [All Commands](../tools/all_commands):Convert \>Lowercase
- Toolbar: None
- Status Bar: None
- Default Keyboard Shortcut: CTRL+U

## Plug-in Command ID

```
EEID_MAKE_LOWER (4150)```

## Macros

## \[JavaScript\]

```
document.selection.ChangeCase(eeCaseLowerCase);
```

## \[VBScript\]

```
document.selection.ChangeCase eeCaseLowerCase
```
