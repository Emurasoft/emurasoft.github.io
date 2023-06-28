# REG\_SET\_VALUE\_INFO

用于 [EE\_REG\_SET\_VALUE 消息](../message/ee_reg_set_value)。

typedef struct \_REG\_SET\_VALUE\_INFO {

size\_t cbSize;

DWORD dwKey;

LPCWSTR pszConfig;

LPCWSTR pszValue;

DWORD dwType;

const BYTE\* lpData;

DWORD cbData;

DWORD dwFlags;

} REG\_SET\_VALUE\_INFO;

## 成员

_cbSize_

> 以字节为单位的数据结构大小。把这个成员设为 sizeof( REG\_SET\_VALUE\_INFO )。

_dwKey_

> 用下列值之一指定一个键值。EEREG\_CONFIG 和 EEREG\_EMEDITORPLUGIN 需要 pszConfig 参数来指定键值。
>
> |     |     |
> | --- | --- |
> | EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common 或 eeCommon.ini\\\[Common\] |
> | EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist 或 eeCommon.ini\\\[Regist\] |
> | EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros 或 eeCommon.ini\\\[Macros\] |
> | EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns 或 eeCommon.ini\\\[PlugIns\] |
> | EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List 或 eeCommon.ini\\\[Recent File List\] |
> | EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List 或 eeCommon.ini\\\[Recent Folder List\] |
> | EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List 或 eeCommon.ini\\\[Recent Font List\] |
> | EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List 或 eeCommon.ini\\\[Recent Insert List\] |
> | EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave 或 eeCommon.ini\\\[AutoSave\] |
> | EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common 或 eeLM.ini\\\[Common\] |
> | EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist 或 eeLM.ini\\\[Regist\] |
> | EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) 或 eeConfig.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) 或 eePlugin.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) 或 eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

> 用一个额外的字符串来指定键值当 when EEREG\_CONFIG，EEREG\_EMEDITORPLUGIN，或 EEREG\_EMEDITORUSERS 被选取时。

_pszValue_

> 指定要被设置的值的名称。如果该参数是 NULL 并且 dwType 参数是 REG\_SZ，dwKey 和 pszConfig 参数所指向的整个键值包括这个键值内的所有条目都会被删除。

_dwType_

> 用下列值之一来指定 lpData 参数指向的数据类型。
>
> |     |     |
> | --- | --- |
> | REG\_BINARY | 任何形式的二进制数据。 |
> | REG\_DWORD | 一个 32 位数字。 |
> | REG\_SZ | 一个以 null 结尾的 Unicode 字符串。 |

_lpData_

> 被储存的数据。对于 REG\_SZ 类型，字符串必须是以 null 结尾。

_cbData_

> 由 lpData 参数指向的以字节为单位的信息大小。如果该数据是 REG\_SZ 类型，cbData 必须得包括终止空字符的大小。

_dwFlags_

> 这个参数可以是 EE\_REG\_VARIABLE\_SIZE 如果二进制数据是一个可变的大小。否则的话，它必须是零。

## 版本

> 支持 EmEditor 7.00 或之后的版本。