# EXEC\_PLUGIN\_INFO

用于 [EE\_EXEC\_PLUGIN](../message/ee_exec_plugin) 消息。

```
typedef struct _EXEC_PLUGIN_INFO {
	UINT cbSize;
	LONG nFlags;
	LPCWSTR pszName;
	WPARAM wParam;
	LPARAM lParam;
	LONG_PTR nResult;
} EXEC_PLUGIN_INFO;
```

## 字段

_cbSize_

指定该结构的大小，sizeof( EE\_PLUGIN\_INFO )。

_nFlags_

指定一个下列值的组合。eePluginExecuteCommand，eePluginUserMessage，和 eePluginQueryStatus 一定要专门指定。

|     |     |
| --- | --- |
| PLUGIN\_FLAG\_EXEC\_COMMAND | 如同选择插件命令一样运行插件。如果指定该值，那么忽略 wParam 和 lParam 参数。 |
| PLUGIN\_FLAG\_USER\_MSG | 用 wParam 和 lParam 参数发送消息至插件。 |
| PLUGIN\_FLAG\_QUERY\_STATUS | 检索插件状态。如果指定该值，那么忽略 wParam 和 lParam 参数。 |
| PLUGIN\_FLAG\_ABSOLUTE\_PATH | pszName 包含文件的完整路径。如果不指定这个标志，插件一定要在默认插件文件夹中，即 EmEditor 安装文件夹中的 PlugIns 子文件夹中。 |

_pszName_

指定插件文件名。

_wParam_

指定第一个送至插件的参数。参数的含义取决于插件。

_lParam_

指定第二个送至插件的参数。参数的含义取决于插件。

## 版本

支持 EmEditor Professional 15.5 或之后的版本。
