# 下一個文檔命令

## 摘要

切換到下一個文檔。

## 說明

切換到下一個打開的 EmEditor 文檔。
這個命令的行為取決于 [點擊 \[下一個文檔\] 命令時切換到上次使用的文檔視窗 核取方塊](../../dlg/customize/window/index) 是否被勾選。如果該核取方塊被勾選，那么使用這個命令會切換到上次最後使用的文檔。如果沒有被勾選，使用這個命令會切換到下一個顯示在索引標籤欄上的文檔。

## 運行方法

- 預設功能表:視窗 \>下一個文檔
- [全部命令](../tools/all_commands):視窗
\>文檔導航
\>下一個文檔
- 工具列: 無
- 狀態列: 無
- 預設捷徑: CTRL+TAB

## 外掛程式命令 ID

- EEID\_NEXT\_WINDOW (4245)

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4245);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4245
```
