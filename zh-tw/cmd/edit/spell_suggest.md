# 拼字建議命令

## 摘要

選擇正確的拼字建議 (多個項目)。

## 說明

選擇正確的拼字建議，并用選取的建議取代拼字不正確的字詞。(這個指令不會取代整個文檔中的拼錯的字)。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):編輯 \>拼字檢查 \>(拼字建議)
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
從 EEID_SPELL_SUGGEST 到 EEID_SPELL_SUGGEST + 31 (從 8768 到 8768 + 31)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(8768 + i);  // i 是一個從 0 到 31 的整數
```

### \[VBScript\]

```
editor.ExecuteCommandByID 8768 + i  ' i 是一個從 0 到 31 的整數
```
