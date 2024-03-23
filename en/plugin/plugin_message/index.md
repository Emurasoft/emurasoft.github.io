# Messages to Plug-ins

|     |     |
| --- | --- |
| [EP\_DISABLE\_AUTO\_COMPLETE](ep_disable_auto_complete) | Queries whether the auto complete for brackets/quotation marks feature should be disabled. |
| [EP\_GET\_BITMAP](ep_get_bitmap) | Retrieves bitmap resource IDs for various sizes and color depths for the plug-in displayed on a toolbar. |
| [EP\_GET\_INFO](ep_get_info) | Retrieves information about the plug-in. |
| [EP\_GET\_MASK](ep_get_mask) | Retrieves mask color for the plug-in button on a toolbar. |
| [EP\_GET\_NAME](ep_get_name) | Retrieves the plug-in name. |
| [EP\_GET\_VERSION](ep_get_version) | Retrieves the plug-in version. |
| [EP\_QUERY\_PROPERTIES](ep_query_properties) | Queries whether the property is enabled. |
| [EP\_QUERY\_UNINSTALL](ep_query_uninstall) | Queries whether the plug-in can be uninstalled. |
| [EP\_SET\_PROPERTIES](ep_set_properties) | Requests the plug-in to display the properties. |
| [EP\_SET\_UNINSTALL](ep_set_uninstall) | Uninstalls the plug-in. |
| [EP\_PRE\_TRANSLATE\_MSG](ep_pre_translate_msg) | Called before each Windows message is translated. |
| [EP\_USE\_DROPPED\_FILES](ep_use_dropped_files) | Queries whether the plug-in wants to use dropped files. |
| [EP\_USER\_MSG](ep_user_msg) | Sends the plug-in user-defined messages. |
| [EP\_SYNC\_NOW](ep_sync_now) | Instructs the plug-in to sync now if the sync feature is supported. |

These messages are used by [Functions to Export PlugInProc](../exports/index).

These constants are defined in the header file (plugin.h).


```{toctree}
:maxdepth: 1
:hidden:
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
