# AI Prompts command

## Summary

Asks a specified AI prompt (multiple items).

## Description

This command consists of multiple menu items. You can run this command to ask an AI prompt defined in the [**AI Prompts** page](../../dlg/customize/ai_list/index) of the **Customize** dialog box. When you run this command, it asks the AI ​​a question using the AI ​​prompt you specified.

## How to Run

- Default Menu: **Tools** \> **AI** \> **(AI prompt)**
- [All Commands](all_commands): **AI** \> **(AI prompt)**
- Toolbar: Each button on the AI toolbar
- Status Bar: None
- Default Shortcut Key: None

## Plug-in Command ID

```
From EEID_AI_ITEM1 through EEID_AI_ITEM1 + 1023 (from 29184 through 29184 + 1023)```

## Macros

### \[JavaScript\]

```
editor.ExecuteCommandByID(29184+i);  // i is an integer from 0 through
1023
```

### \[VBScript\]

```
editor.ExecuteCommandByID 29184+i  ' i is an integer from 0 through 1023
```
