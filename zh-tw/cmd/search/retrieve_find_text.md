# 設置單字為尋找字串命令

## 摘要

把目前的單字設置為查詢字串。

## 說明

設置目前的游標所在處的單字為查詢字串，并用於為 [**尋找下一個** 命令](edit_repeat)。在執行這個命令之後，如果您再選擇 [**尋找下一個** 命令](edit_repeat)，它會馬上尋找下一個與用該命令所指定的單字元合的結果。如果在 [**尋找** 對話方塊](../../dlg/find/index) 中 **「>」按鈕** 下的功能表中沒有勾選「游標下的單字」，那么 [**尋找** 對話方塊](../../dlg/find/index) 會預設把用這個命令指定的單字作為尋找字串。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **搜索**
\> **設置單字為尋找字串**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_RETRIEVE_FIND_TEXT (4325)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4325);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4325
```
