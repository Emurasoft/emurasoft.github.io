# 定位點化整個文檔命令

## 摘要

把整個文檔中的相同的空格轉換為 Tab。

## 說明

把整個文檔中的相同的空格轉換為 Tab。轉換的空格數與一個 Tab所代表的空格數相同。一個 Tab所代表的空格數可以在 [「 Tab/縮排」 對話方塊](../../dlg/properties/general/indent/index) 中設置。在選擇整個文檔后，該命令與 [定位點化 命令](tabify) 相同，但該命令不會延伸到選取區域以外的地方。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):編輯 \>進階 \>將文檔中的空格轉換為 Tab
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_SPACE_TO_TAB (4355)```

## 巨集

## \[JavaScript\]

```
editor.ExecuteCommandByID(4355);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4355
```
