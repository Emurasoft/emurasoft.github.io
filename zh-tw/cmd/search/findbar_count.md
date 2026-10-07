# 顯示符合的個數 (搜尋工具列) 命令

## 摘要

切換搜尋工具列上的[顯示符合個數]按鈕的狀態。

## 說明

切換工具列上「符合次數」按鈕狀態。當這個命令被激活時，EmEditor 將顯示找到的符合指定字串的數目。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **搜尋** \> **搜尋工具列** \> **顯示符合數目**
- 工具列: ![](../../images/find_count.png) (搜尋工具列)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_FINDBAR_COUNT (4578)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4578);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4578
```
