# REG\_QUERY\_VALUE\_INFO

用於 [EE\_REG\_QUERY\_VALUE 消息](../message/ee_reg_query_value) 中。

```
typedef struct _REG_QUERY_VALUE_INFO {
	size_t cbSize;
	DWORD dwKey;
	LPCWSTR pszConfig;
	LPCWSTR pszValue;
	DWORD dwType;
	BYTE *lpData;
	DWORD *lpcbData;
	DWORD dwFlags;
} REG_QUERY_VALUE_INFO;
```

## 構成

_cbSize_

以位元為單位的數據結構大小。把這個成員設為 sizeof( REG\_QUERY\_VALUE\_INFO )。

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

用一個額外的字符串來指定鍵值當 EEREG\_CONFIG，EEREG\_EMEDITORPLUGIN，或 EEREG\_EMEDITORUSERS 被選取時。

_pszValue_

指定要檢索的值的名稱。

_dwType_

按 lpData 參數用下列值之一來指定被指向的數據類型。

|     |     |
| --- | --- |
| REG\_BINARY | 任何形式的二進制數據。 |
| REG\_DWORD | 一個 32 位數字。 |
| REG\_SZ | 一個以 null 結尾的 Unicode 字符串。 |

_lpData_

一個指針指向接收指定值的數據的緩沖區。只有當數據是 REG\_BINARY 時，這個參數可以是 NULL。

_lpcbData_

一個指針指向一個變量，這個變量以位元為單位表示由 lpData 參數指定的緩沖區的大小。當函數返回時，這個變量包含被複製到 lpData 上的數據大小。

_dwFlags_

該參數被預留，并且必須是零。

## 支持版本

支持 EmEditor 7.00 或之後的版本。
