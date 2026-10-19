# 检查更新命令

## 摘要

连接到 Emurasoft 服务器检查可用的新版本的EmEditor。

## 说明

通过连接到 Emurasoft 的服务器上来检查可用的新版本的 EmEditor。要进行这项操作，必须有网络连接。在 EmEditor 完成更新检查并检测到可更新的新版本后，你会被询问是否要开始更新。

更新检查器将于 2027 年 3 月 31 日 (UTC) 之后停用。在该日期之后，此命令将不可用。

## 运行方法

- 默认菜单: **帮助** \> **检查更新**
- [所有命令](../tools/all_commands): **帮助** >
**检查更新**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_CHECK_UPDATES (4481)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4481);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4481
```
