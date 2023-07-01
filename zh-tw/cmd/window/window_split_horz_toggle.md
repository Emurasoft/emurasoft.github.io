# 切換水平分割命令

### 摘要

> 切換水平視窗分割。

### 說明

> 如果目前的視窗被垂直分割或完全不分割，這個命令將分割把目前的視窗分割成水平窗格，并且會在視窗中心固定分割位置。如果目前的視窗已經被水平分割了，這個命令則會從目前的視窗中移除水平分割。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **視窗**
\> **分割** \> **切換水平分割**
- 工具列: ![](../../images/windowsplithorzfix.gif)
- 狀態列: 無
- 預設捷徑: CTRL + -

### 外掛程式命令 ID

- EEID\_WINDOW\_SPLIT\_HORZ\_TOGGLE (4385)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4385);

#### \[VBScript\]

> editor.ExecuteCommandByID 4385
