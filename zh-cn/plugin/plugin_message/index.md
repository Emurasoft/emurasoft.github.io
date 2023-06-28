# 插件消息

|     |     |
| --- | --- |
| [EP\_DISABLE\_AUTO\_COMPLETE](ep_disable_auto_complete) | 查询括号/引号自动完成功能是否被禁用。 |
| [EP\_GET\_BITMAP](ep_get_bitmap) | 为显示在工具栏上的插件检索位图资源 ID 的各种大小与颜色深度。 |
| [EP\_GET\_INFO](ep_get_info) | 检索有关插件的信息。 |
| [EP\_GET\_MASK](ep_get_mask) | 为在工具栏上的插件按钮检索过滤色。 |
| [EP\_GET\_NAME](ep_get_name) | 检索插件名称。 |
| [EP\_GET\_VERSION](ep_get_version) | 检索插件版本。 |
| [EP\_QUERY\_PROPERTIES](ep_query_properties) | 查询属性是否被启用。 |
| [EP\_QUERY\_UNINSTALL](ep_query_uninstall) | 查询插件是否被卸载。 |
| [EP\_SET\_PROPERTIES](ep_set_properties) | 请求插件显示属性。 |
| [EP\_SET\_UNINSTALL](ep_set_uninstall) | 卸载插件。 |
| [EP\_PRE\_TRANSLATE\_MSG](ep_pre_translate_msg) | 在每一条 Windows 消息被翻译之前召集。 |
| [EP\_USE\_DROPPED\_FILES](ep_use_dropped_files) | 查询插件是否想要用删除的文件。 |
| [EP\_USER\_MSG](ep_user_msg) | 发送插件的用户定义消息。 |
| [EP\_SYNC\_NOW](ep_sync_now) | 如果支持同步功能，则指示插件立即同步。 |

这些消息通过 [导出函数 PlugInProc](../exports/index) 被使用。

这些常数在头文件 (plugin.h) 中被定义。

```{toctree}
:maxdepth: 1
ep_disable_auto_complete
ep_get_bitmap
ep_get_info
ep_get_mask
ep_get_name
ep_get_version
ep_pre_translate_msg
ep_query_properties
ep_query_uninstall
ep_set_properties
ep_set_uninstall
ep_sync_now
ep_use_dropped_files
ep_user_msg
```
