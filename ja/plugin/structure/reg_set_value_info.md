# REG\_SET\_VALUE\_INFO

[EE\_REG\_SET\_VALUE メッセージ](../message/ee_reg_set_value) で使用します。

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

## フィールド

_cbSize_

このデータ構造体のサイズをバイト数で指定します。sizeof(REG\_SET\_VALUE\_INFO) を指定します。

_dwKey_

以下の値のいずれかを指定して、キーを指定します。EEREG\_CONFIG および EEREG\_EMEDITORPLUGIN には pszConfig パラメータが必要です。

|     |     |
| --- | --- |
| EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common または eeCommon.ini\\\[Common\] |
| EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist または eeCommon.ini\\\[Regist\] |
| EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros または eeCommon.ini\\\[Macros\] |
| EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns または eeCommon.ini\\\[PlugIns\] |
| EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List または eeCommon.ini\\\[Recent File List\] |
| EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List または eeCommon.ini\\\[Recent Folder List\] |
| EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List または eeCommon.ini\\\[Recent Font List\] |
| EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List または eeCommon.ini\\\[Recent Insert List\] |
| EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave または eeCommon.ini\\\[AutoSave\] |
| EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common または eeLM.ini\\\[Common\] |
| EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist または eeLM.ini\\\[Regist\] |
| EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) または eeConfig.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) または eePlugin.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) または eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

EEREG\_CONFIG、EEREG\_EMEDITORPLUGIN または EEREG\_EMEDITORUSERS が選択されたとき、キーを指定するための追加の文字列を指定します。

_pszValue_

設定する値の名前を指定します。このパラメータが NULL で dwType パラーメータが REG\_SZ なら、dwKey パラメータと pszConfig パラメータで指定されたすべてのエントリを含むキーは削除されます。

_dwType_

以下の値のいずれかを選択し、lpData パラメータのデータの種類を指定します。

|     |     |
| --- | --- |
| REG\_BINARY | 様々なフォームのバイナリ データ |
| REG\_DWORD | 32 ビット数 |
| REG\_SZ | ヌル文字で終了する Unicode 文字列 |

_lpData_

保存するデータを指定します。REG\_SZ の種類では、ヌル文字で終了する必要があります。このパラメータが NULL の場合、pszValue パラメータで示された値は削除されます。

_cbData_

lpData パラメータで示された情報のサイズをバイト数で指定します。データが REG\_SZ の種類の場合、cbData は終端ヌル文字を含めたサイズを指定する必要があります。

_dwFlags_

バイナリ データが可変サイズの場合、このパラメータには EE\_REG\_VARIABLE\_SIZE を指定します。それ以外の場合、0 を指定する必要があります。

## バージョン

Version 7.00 以上で利用できます。
