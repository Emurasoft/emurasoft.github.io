# Editor\_RegSetValue

根據 EmEditor 的設定，設一個值到注冊表或一個 INI 檔案中。您能直接用該內嵌函式或明確地發送 [EE\_REG\_SET\_VALUE](../message/ee_reg_set_value) 消息。

Editor\_RegSetValue( HWND hwnd, DWORD dwKey, LPCWSTR pszConfig, LPCWSTR pszValue, DWORD dwType, const BYTE\* lpData, DWORD cbData, DWORD dwFlags );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_dwKey_

用下列值之一來指定一個鍵值。EEREG\_CONFIG 和 EEREG\_EMEDITORPLUGIN 需要 pszConfig 參數來指定鍵值。

|     |     |
| --- | --- |
| EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common or eeCommon.ini\\\[Common\] |
| EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist or eeCommon.ini\\\[Regist\] |
| EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros or eeCommon.ini\\\[Macros\] |
| EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns or eeCommon.ini\\\[PlugIns\] |
| EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List or eeCommon.ini\\\[Recent File List\] |
| EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List or eeCommon.ini\\\[Recent Folder List\] |
| EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List or eeCommon.ini\\\[Recent Font List\] |
| EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List or eeCommon.ini\\\[Recent Insert List\] |
| EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave or eeCommon.ini\\\[AutoSave\] |
| EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common or eeLM.ini\\\[Common\] |
| EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist or eeLM.ini\\\[Regist\] |
| EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) or eeConfig.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) or eePlugins.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) or eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

用一個額外的字串來指定鍵值當 EEREG\_CONFIG，EEREG\_EMEDITORPLUGIN，或 EEREG\_EMEDITORUSERS 被選取時。

_pszValue_

指定要被設置的值的名稱。如果該參數是 NULL 并且 dwType 參數是 REG\_SZ，dwKey 和 pszConfig 參數所指向的整個鍵值包括這個鍵值內的所有項目都會被刪除。

_dwType_

用下列值之一來指定 lpData 參數指向的數據類型。

|     |     |
| --- | --- |
| REG\_BINARY | 任何形式的二進位數據。 |
| REG\_DWORD | 一個 32 位數字。 |
| REG\_SZ | 一個以 null 結尾的 Unicode 字串。 |

_lpData_

被儲存的數據。對于 REG\_SZ 類型，字串必須是以 null 結尾。如果該參數是 NULL,由 pszValue 參數指向的值會被移除。

_cbData_

由 lpData 參數指向的以位元為單位的信息大小。如果該數據是 REG\_SZ 類型，cbData 必須得包括終止空字元的大小。

_dwFlags_

這個參數可以是 EE\_REG\_VARIABLE\_SIZE 如果二進位數據是一個可變的大小。否則的話，它必須是零。

## 返回值

如果消息成功，返回值是 ERROR\_SUCCESS。

如果消息不成功，返回值是一個在 Winerror.h 中被定義的非零錯誤代碼。

## 支持版本

支持 EmEditor 7.00 或之後的版本。
