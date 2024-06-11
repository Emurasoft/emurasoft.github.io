# AI 提示命令

## 摘要

詢問指定的 AI 提示(多個項目)。

## 說明

此命令包含多個功能表項。您可以運行此命令來詢問在 **自訂** 對話方塊的 [**AI 提示** 頁面](../../dlg/customize/ai_list/index) 中定義的 AI 提示。當您運行此命令時，它會使用您指定的 AI 提示向 AI 提問。

## 運行方法

- 預設功能表: **工具** \> **AI** \> **(AI 提示)**
- [所有命令](all_commands): **AI** \> **(AI 提示)**
- 工具列: AI 工具列上的每個按鈕
- 狀態列: 無
- 預設快速鍵: 無

## 外掛程式命令 ID

```
From EEID_AI_ITEM1 through EEID_AI_ITEM1 + 1023 (從 29184 到 29184 + 1023)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(29184+i);  // i 是一個從 0 到 1023 的整數
```

### \[VBScript\]

```
editor.ExecuteCommandByID 29184+i  ' i 是一個從 0 到 1023 的整數
```