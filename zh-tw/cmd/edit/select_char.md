# 選擇字元命令

## 摘要

切換字元選擇模式。

## 說明

切換字元選擇模式。這個命令讓您能用鍵盤亮顯多個字元。用箭頭鍵移動游標來延伸或縮短選區。選擇 [**複製** 命令](edit_copy) 或 [**剪下** 命令](edit_cut) 將終止字元選擇模式。這個命令等同于按住 SHIFT 鍵和任何一個箭頭鍵。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選區**
\> **選擇字元**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: F8

## 外掛程式命令ID

```
EEID_SELECT_CHAR (4153)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4153);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4153
```
