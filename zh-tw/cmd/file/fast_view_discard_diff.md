# 捨棄差異命令

## 摘要

捨棄快速檢視模式的編輯內容並刪除差異檔。

## 說明

此命令可在快速檢視模式中，當文檔有編輯內容或目前檔案的差異檔存在時使用。在您確認之後，EmEditor 會捨棄文檔的編輯內容（包括儲存在差異檔中的編輯內容），並刪除差異檔。原始檔案不會變更。

若要刪除未開啟之檔案的差異檔，請使用 **自訂** 對話方塊的 [**快速檢視** 頁面](../../dlg/customize/fast_view/index)。詳細資訊請參見[在快速檢視模式中開啟和編輯巨型檔案](../../howto/file/file_fast_view)。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **差異** \> **捨棄差異**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_FAST_VIEW_DISCARD_DIFF (23293)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(23293);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 23293
```
