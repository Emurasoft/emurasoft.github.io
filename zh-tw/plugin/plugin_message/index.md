# 外掛程式消息

|     |     |
| --- | --- |
| [EP\_DISABLE\_AUTO\_COMPLETE](ep_disable_auto_complete) | 查詢括號/引號自動完成功能是否被禁用。 |
| [EP\_GET\_BITMAP](ep_get_bitmap) | 為顯示在工具列上的外掛程式檢索位圖資源 ID 的各種大小與顏色深度。 |
| [EP\_GET\_INFO](ep_get_info) | 檢索有關外掛程式的信息。 |
| [EP\_GET\_MASK](ep_get_mask) | 為在工具列上的外掛程式按鈕檢索過濾色。 |
| [EP\_GET\_NAME](ep_get_name) | 檢索外掛程式名稱。 |
| [EP\_GET\_VERSION](ep_get_version) | 檢索外掛程式版本。 |
| [EP\_QUERY\_PROPERTIES](ep_query_properties) | 查詢屬性是否被啟用。 |
| [EP\_QUERY\_UNINSTALL](ep_query_uninstall) | 查詢外掛程式是否被卸載。 |
| [EP\_SET\_PROPERTIES](ep_set_properties) | 請求外掛程式顯示屬性。 |
| [EP\_SET\_UNINSTALL](ep_set_uninstall) | 卸載外掛程式。 |
| [EP\_PRE\_TRANSLATE\_MSG](ep_pre_translate_msg) | 在每一條 Windows 消息被翻譯之前召集。 |
| [EP\_USE\_DROPPED\_FILES](ep_use_dropped_files) | 查詢外掛程式是否想要用刪除的檔案。 |
| [EP\_USER\_MSG](ep_user_msg) | 發送外掛程式的使用者定義消息。 |
| [EP\_SYNC\_NOW](ep_sync_now) | 如果支持同步功能，則指示外掛程式立即同步。 |

這些消息通過 [導出函數 PlugInProc](../exports/index) 被使用。

這些常數在頭檔案 (plugin.h) 中被定義。


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
