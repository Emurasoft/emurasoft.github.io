# Editor\_ExecPlugin

執行一個指定的外掛程式。你能直接用該內嵌函式或明確地發送 [EE\_EXEC\_PLUGIN](../message/ee_exec_plugin) 消息。

HRESULT Editor\_ExecPlugin( HWND hwnd, LPCWSTR pszName, LONG nFlags, WPARAM wParam, LPARAM lParam, LONG\_PTR\* pnResult );

## 參數

_hwnd_

> 指定 EmEditor 視圖或方塊架的視窗控制代碼。

_pszName_

> 指定外掛程式檔案名。

_nFlags_

> 指定一個下列值的組合。PLUGIN\_FLAG\_EXEC\_COMMAND，PLUGIN\_FLAG\_USER\_MSG，和 PLUGIN\_FLAG\_QUERY\_STATUS 一定要專門指定。
>
> |     |     |
> | --- | --- |
> | PLUGIN\_FLAG\_EXEC\_COMMAND | 如同選擇外掛程式命令一樣運行外掛程式。如果指定該值，那么忽略 wParam 和 lParam 參數。 |
> | PLUGIN\_FLAG\_USER\_MSG | 用 wParam 和 lParam 參數發送消息至外掛程式。 |
> | PLUGIN\_FLAG\_QUERY\_STATUS | 檢索外掛程式狀態。如果指定該值，那么忽略 wParam 和 lParam 參數。 |
> | PLUGIN\_FLAG\_ABSOLUTE\_PATH | pszName 包含檔案的完整路徑。如果不指定這個標志，外掛程式一定要在預設外掛程式資料夾中，即 EmEditor 安裝資料夾中的 PlugIns 子資料夾中。 |

_wParam_

> 指定第一個送至外掛程式的參數。參數的含義取決于外掛程式。

_lParam_

> 指定第二個送至外掛程式的參數。參數的含義取決于外掛程式。

## 返回值

> 如果發生錯誤，返回值是負值。如果指定的是 PLUGIN\_FLAG\_EXEC\_COMMAND，返回值為 0。如果指定 PLUGIN\_FLAG\_USER\_MSG，返回值的含義取決于外掛程式。如果指定 PLUGIN\_FLAG\_QUERY\_STATUS，返回值則會是下列值的組合。
>
> |     |     |
> | --- | --- |
> | STATUS\_ENABLED | 啟用外掛程式。 |
> | STATUS\_LATCHED | 勾選外掛程式。 |

## 版本

> 支持 EmEditor Professional Version 15.5 或之後的版本。
