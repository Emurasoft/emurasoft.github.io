# Editor\_RegSetValue

根据 EmEditor 的设定，设一个值到注册表或一个 INI 文件中。你能直接用该内联函数或明确地发送 [EE\_REG\_SET\_VALUE](../message/ee_reg_set_value) 消息。

Editor\_RegSetValue( HWND hwnd, DWORD dwKey, LPCWSTR pszConfig, LPCWSTR pszValue, DWORD dwType, const BYTE\* lpData, DWORD cbData, DWORD dwFlags );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_dwKey_

> 用下列值之一来指定一个键值。EEREG\_CONFIG 和 EEREG\_EMEDITORPLUGIN 需要 pszConfig 参数来指定键值。
>
> |     |     |
> | --- | --- |
> | EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common or eeCommon.ini\\\[Common\] |
> | EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist or eeCommon.ini\\\[Regist\] |
> | EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros or eeCommon.ini\\\[Macros\] |
> | EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns or eeCommon.ini\\\[PlugIns\] |
> | EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List or eeCommon.ini\\\[Recent File List\] |
> | EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List or eeCommon.ini\\\[Recent Folder List\] |
> | EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List or eeCommon.ini\\\[Recent Font List\] |
> | EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List or eeCommon.ini\\\[Recent Insert List\] |
> | EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave or eeCommon.ini\\\[AutoSave\] |
> | EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common or eeLM.ini\\\[Common\] |
> | EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist or eeLM.ini\\\[Regist\] |
> | EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) or eeConfig.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) or eePlugins.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) or eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

> 用一个额外的字符串来指定键值当 EEREG\_CONFIG，EEREG\_EMEDITORPLUGIN，或 EEREG\_EMEDITORUSERS 被选取时。

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

> 被储存的数据。对于 REG\_SZ 类型，字符串必须是以 null 结尾。如果该参数是 NULL,由 pszValue 参数指向的值会被移除。

_cbData_

> 由 lpData 参数指向的以字节为单位的信息大小。如果该数据是 REG\_SZ 类型，cbData 必须得包括终止空字符的大小。

_dwFlags_

> 这个参数可以是 EE\_REG\_VARIABLE\_SIZE 如果二进制数据是一个可变的大小。否则的话，它必须是零。

## 返回值

> 如果消息成功，返回值是 ERROR\_SUCCESS。
>
> 如果消息不成功，返回值是一个在 Winerror.h 中被定义的非零错误代码。

## 支持版本

支持 EmEditor 7.00 或之后的版本。
