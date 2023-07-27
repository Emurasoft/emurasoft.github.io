# 外掛程式清單命令

## 摘要

運行一個指定的外掛程式 (多個項目) 。

## 說明

這個命令由多個功能表項目組成。該命令會執行指定的外掛程式。可用的外掛程式可以在 [自訂外掛程式 對話方塊](../../dlg/plugins/index) 中定義。

## 運行方法

- 預設功能表:外掛程式 \> (外掛程式名稱)
- [所有命令](all_commands):外掛程式 \> (外掛程式名稱)
- 工具列: 外掛程式工具列上的按鈕
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
From EEID_PLUG_IN1 through EEID_PLUG_IN1 + 255 (從 5632 到 5632 + 255)```

## 巨集

## \[JavaScript\]

```
editor.ExecuteCommandByID(5632+i);  // i 是從 0 到 255 的整數
```

## \[VBScript\]

```
editor.ExecuteCommandByID 5632+i  ' i 是從 0 到 255 的整數
```
