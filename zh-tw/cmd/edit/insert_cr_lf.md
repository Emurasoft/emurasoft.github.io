# 插入 CR 和 LF 命令

### 摘要

> 在游標位置插入歸位與換行。

### 說明

> 在目前的游標位置處插入一個歸位 (CR) 和一個換行符 (LF)。EmEditor 可以編輯同時有 CR 和 LF 作為換行的文件。按一下歸位鍵 (ENTER) 在目前的行插入相同的換行方式，僅 CR，僅 LF，或 CR+LF。這個命令會一直插入 CR+LF 的換行方式，無論在當期行使用的是哪一種換行方式。

### 運行方法

- 預設功能表: **插入** \> **CR和LF**
- [全部命令](../tools/all_commands): **插入** \> **CR和LF**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

### 外掛程式命令ID

- EEID\_INSERT\_CR\_LF (4274)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4274);

#### \[VBScript\]

> editor.ExecuteCommandByID 4274