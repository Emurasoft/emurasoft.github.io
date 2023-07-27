# OEM/DOS 字型命令

## 摘要

以 OEM/DOS 字型顯示文字。

## 說明

從字型分類中選擇 OEM/DOS 字型。每一個字型分類中的字型可以在 [自訂字型 對話方塊](../../dlg/properties/font/index) 中被設定。變更字型分類將不會改變打開檔案的編碼。如果您想要變更編碼并重新載入檔案，選擇 [重新載入 (多個項目) 命令](../file/file_reload_defined)。

## 運行方法

- 預設功能表:檢視 \>字型分類 \>OEM/DOS
- [全部命令](../tools/all_commands):檢視 \>字型 >
字型分類
\>OEM/DOS
- 工具列: ![](../../images/fontpopup.gif) (點擊箭頭) \>字型分類 \>OEM/DOS
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_CHARSET_OEM (8719)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(8719);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 8719
```
