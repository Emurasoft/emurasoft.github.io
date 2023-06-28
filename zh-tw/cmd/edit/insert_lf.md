# 插入 LF 命令

### 摘要

> 在游標處插入 LF。

### 說明

> 在目前的游標位置處插入一個換行符 (LF)。EmEditor 可以編輯同時有 CR 和 LF 作為換行的文件。按一下歸位鍵 (ENTER) 在目前的行插入相同的換行方式，僅 CR，僅 LF，或 CR+LF。這個命令會一直插入僅 LF 的換行方式，無論在當期行使用的是哪一種換行方式。

### 運行方法

- 預設功能表: **插入** \> **僅 LF**
- [全部命令](../tools/all_commands): **插入** \> **僅 LF**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

### 外掛程式命令ID

- EEID\_INSERT\_LF (4146)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4146);

#### \[VBScript\]

> editor.ExecuteCommandByID 4146