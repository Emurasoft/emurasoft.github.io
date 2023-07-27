# 字型清單命令

## 摘要

選擇最近使用過的字型 (多個項目) 。

## 說明

這個命令有多個功能表項目組成，會顯示一清單的最近使用的字型。這個命令會選擇指定的字型。顯示的字型數可以到工具 功能表下 [自訂 對話方塊](../../dlg/customize/index) 中 [歷史記錄 頁面](../../dlg/customize/history/index) 上的最近使用的字型數 文字方塊中設定。 (工具 \>自訂 \>歷史記錄) 。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):檢視 \>字型 >
最近使用的字型 \> (最近使用的字型)
- 工具列: ![](../../images/fontpopup.gif) (點擊箭頭) \> (最近使用的字型)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
從 EEID_MRU_FONT1 到 ID_MRU_FONT1 + 63 (從 4736 到 4736 + 63)```

## 巨集

## \[JavaScript\]

```
editor.ExecuteCommandByID(4736 + i); // i是從0到63的整數
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4736 + i   '
i是從0到63的整數
```
