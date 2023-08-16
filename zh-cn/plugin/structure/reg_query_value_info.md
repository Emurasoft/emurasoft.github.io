# REG\_QUERY\_VALUE\_INFO

用于 [EE\_REG\_QUERY\_VALUE 消息](../message/ee_reg_query_value) 中。

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

## 成员

_cbSize_

以字节为单位的数据结构大小。把这个成员设为 sizeof( REG\_QUERY\_VALUE\_INFO )。

_dwKey_

用下列值之一来指定一个键值。EEREG\_CONFIG 和 EEREG\_EMEDITORPLUGIN 需要 pszConfig 参数来指定键值。

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

用一个额外的字符串来指定键值当 EEREG\_CONFIG，EEREG\_EMEDITORPLUGIN，或 EEREG\_EMEDITORUSERS 被选取时。

_pszValue_

指定要检索的值的名称。

_dwType_

按 lpData 参数用下列值之一来指定被指向的数据类型。

|     |     |
| --- | --- |
| REG\_BINARY | 任何形式的二进制数据。 |
| REG\_DWORD | 一个 32 位数字。 |
| REG\_SZ | 一个以 null 结尾的 Unicode 字符串。 |

_lpData_

一个指针指向接收指定值的数据的缓冲区。只有当数据是 REG\_BINARY 时，这个参数可以是 NULL。

_lpcbData_

一个指针指向一个变量，这个变量以字节为单位表示由 lpData 参数指定的缓冲区的大小。当函数返回时，这个变量包含被复制到 lpData 上的数据大小。

_dwFlags_

该参数被预留，并且必须是零。

## 版本

支持 EmEditor 7.00 或之后的版本。
