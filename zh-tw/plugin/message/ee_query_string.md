# EE\_QUERY\_STRING

查詢與指定的命令相關聯的字串。您能明確地發送該消息或用 [Editor\_QueryString](../macro/editor_querystring) 內嵌函式。

EE\_QUERY\_STRING

wParam = (WPARAM) MAKEWPARAM( nCmdID, bShortTitle );

lParam = (LPARAM) (LPWSTR) psz;

## 參數

_nCmdID_

指定一個表示要執行的命令 ID 的整數。只能使用下列命令。詳細信息請訪問 **[命令參考](../../cmd/index)**。

|     |     |     |
| --- | --- | --- |
| nID | 命令名稱 | 返回值 |
| 4609 到 4609 + 63 | [**最近文檔清單**](../../cmd/file/file_mru_file1) | 檔案路徑和名稱 |
| 4864 到 4864 + 63 | [**要插入的最近檔案清單**](../../cmd/file/file_mru_insert1) | 檔案路徑和名稱 |
| 4992 到 4992 + 63 | [**最近資料夾清單**](../../cmd/file/file_mru_folder1) | 檔案路徑和名稱 |
| 5376 到 5376 + 255 | **[文檔清單命令](../../cmd/window/window_menu)** | 視窗標題 |
| 5632 到 5632 + 255 | **[外掛程式清單命令](../../cmd/tools/plug_in1)** | 外掛程式檔名稱 |
| 6656 到 6656 + 255 | [**要重新載入的編碼清單命令**](../../cmd/file/file_reload_defined) | 編碼名稱 |
| 7680 到 7680 + 255 | [**要儲存的編碼清單**](../../cmd/file/file_save_defined) | 編碼名稱 |
| 9216 到 9216 + 1023 | **[巨集清單命令](../../cmd/macros/macro1)** | 巨集路徑和名稱 |

_bShortTitle_

指定是否在特定命令中需要字串的簡短版本。

_psz_

指定要檢索字串的緩沖區。

## 返回值

如果命令 ID 有效，返回值是非零。否則的話，返回值是零。

## 支持版本

支持 EmEditor 7.00 或之後的版本。
