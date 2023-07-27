# EXEC\_PLUGIN\_INFO

用於 [EE\_EXEC\_PLUGIN](../message/ee_exec_plugin) 消息。

typedef struct \_EXEC\_PLUGIN\_INFO {

UINT cbSize;

LONG nFlags;

LPCWSTR pszName;

WPARAM wParam;

LPARAM lParam;

LONG\_PTR nResult;

} EXEC\_PLUGIN\_INFO;

## 字段

_cbSize_

指定該結構的大小，sizeof( EE\_PLUGIN\_INFO )。

_nFlags_

指定一個下列值的組合。eePluginExecuteCommand，eePluginUserMessage，和 eePluginQueryStatus 一定要專門指定。

|     |     |
| --- | --- |
| PLUGIN\_FLAG\_EXEC\_COMMAND | 如同選擇外掛程式命令一樣運行外掛程式。如果指定該值，那么忽略 wParam 和 lParam 參數。 |
| PLUGIN\_FLAG\_USER\_MSG | 用 wParam 和 lParam 參數發送消息至外掛程式。 |
| PLUGIN\_FLAG\_QUERY\_STATUS | 檢索外掛程式狀態。如果指定該值，那么忽略 wParam 和 lParam 參數。 |
| PLUGIN\_FLAG\_ABSOLUTE\_PATH | pszName 包含檔案的完整路徑。如果不指定這個標志，外掛程式一定要在預設外掛程式資料夾中，即 EmEditor 安裝資料夾中的 PlugIns 子資料夾中。 |

_pszName_

指定外掛程式檔案名。

_wParam_

指定第一個送至外掛程式的參數。參數的含義取決于外掛程式。

_lParam_

指定第二個送至外掛程式的參數。參數的含義取決于外掛程式。

## 版本

支持 EmEditor Professional 15.5 或之後的版本。
