# QUERY\_STRING\_INFO

用於 [EE\_QUERY\_STRING\_EX 消息](../message/ee_query_string_ex) 中。

typedef struct \_QUERY\_STRING\_INFO {

UINT cbSize;

UINT nCmdID;

UINT nFlags;

UINT cchBuf;

LPWSTR pBuf;

} QUERY\_STRING\_INFO;

## 成員

_cbSize_

以位元組為單位的數據結構大小。把這個成員設為 sizeof( QUERY\_STRING\_INFO )。

_nCmdID_

指定一個表示要執行的命令 ID 的整數。只能使用下列命令。詳細信息請訪問
**[命令參考](../../cmd/index)**。

|     |     |     |
| --- | --- | --- |
| nID | 命令名稱 | 返回值 |
| 4609 到 4609 + 63 | [**最近文檔清單**](../../cmd/file/file_mru_file1) | 檔案路徑和名稱 |
| 4864 到 4864 + 63 | [**要插入的最近檔案清單**](../../cmd/file/file_mru_insert1) | 檔案路徑和名稱 |
| 4992 到 4992 + 63 | [**最近資料夾清單**](../../cmd/file/file_mru_folder1) | 檔案路徑和名稱 |
| 5376 到 5376 + 255 | **[文檔清單命令](../../cmd/window/window_menu)** | 視窗標題 |
| 5632 到 5632 + 255 | **[外掛程式清單命令](../../cmd/tools/plug_in1)** | 外掛程式檔案名稱 |
| 6656 到 6656 + 255 | [**要重新載入的編碼清單命令**](../../cmd/file/file_reload_defined) | 編碼名稱 |
| 7680 到 7680 + 255 | [**要儲存的編碼清單**](../../cmd/file/file_save_defined) | 編碼名稱 |
| 9216 到 9216 + 1023 | **[巨集清單命令](../../cmd/macros/macro1)** | 巨集路徑和名稱 |

_nFlags_

指定以下值之一。

|     |     |
| --- | --- |
| QUERY\_STRING\_LONG\_TITLE | 指定需要該字串的長版本。 |
| QUERY\_STRING\_SHORT\_TITLE | 指定需要該字串的簡短版本。 |

_cchBuf_

指定以字元為單位的緩沖區大小。

_pBuf_

指定用於檢索字串的緩沖區。

## 支持版本

支持 EmEditor Professional Version 20.6 或之後的版本。
