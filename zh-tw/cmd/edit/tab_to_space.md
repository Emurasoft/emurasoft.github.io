# 將所有 Tab 轉換為空格命令

## 摘要

轉換整個檔案中的 Tab 為空格。

## 說明

把整個文檔中所有行開頭出的 Tab轉換為空格。一個 Tab 所代表的空格數可以在 [**「 Tab/縮排」** 對話方塊](../../dlg/properties/general/indent/index) 中設置。在選擇整個文檔后，該命令與 [**非定位點化** 命令](../convert/untabify) 相同，但該命令不會延伸到選取區域以外的地方。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **進階** \> **將文件中的定位點轉空白**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_TAB_TO_SPACE (4253)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4253);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4253
```
