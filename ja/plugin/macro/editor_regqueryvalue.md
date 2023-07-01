# Editor\_RegQueryValue

EmEditor の設定に応じて、レジストリまたは INI ファイルから、指定する値を取得します。このインライン関数を使うか、または
[EE\_QUERY\_VALUE メッセージ](../message/ee_reg_query_value) を直接送ることができます。

Editor\_RegQueryValue( HWND hwnd, DWORD dwKey, LPCWSTR pszConfig, LPCWSTR pszValue, DWORD dwType, BYTE\* lpData, DWORD\* lpcbData, DWORD dwFlags );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_dwKey_

> 以下の値のいずれかを指定して、キーを指定します。EEREG\_CONFIG および EEREG\_EMEDITORPLUGIN には pszConfig パラメータが必要です。
>
> |     |     |
> | --- | --- |
> | EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common または eeCommon.ini\\\[Common\] |
> | EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist または eeCommon.ini\\\[Regist\] |
> | EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros または eeCommon.ini\\\[Macros\] |
> | EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns または eeCommon.ini\\\[PlugIns\] |
> | EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List または eeCommon.ini\\\[Recent File List\] |
> | EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List または eeCommon.ini\\\[Recent Folder List\] |
> | EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List または eeCommon.ini\\\[Recent Font List\] |
> | EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List または eeCommon.ini\\\[Recent Insert List\] |
> | EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave または eeCommon.ini\\\[AutoSave\] |
> | EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common または eeLM.ini\\\[Common\] |
> | EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist または eeLM.ini\\\[Regist\] |
> | EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) または eeConfig.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) または eePlugins.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) または eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

> EEREG\_CONFIG、EEREG\_EMEDITORPLUGIN または EEREG\_EMEDITORUSERS が選択されたとき、キーを指定するための追加の文字列を指定します。

_pszValue_

> 取得する値の名前を指定します。

_dwType_

> 以下の値のいずれかを選択し、lpData パラメータのデータの種類を指定します。
>
> |     |     |
> | --- | --- |
> | REG\_BINARY | 様々なフォームのバイナリ データ |
> | REG\_DWORD | 32 ビット数 |
> | REG\_SZ | ヌル文字で終了する Unicode 文字列 |

_lpData_

> 値のデータを受け取るバッファへのポインタです。このパラメータは、データが REG\_BINARY の種類のときのみヌルにすることができます。

_lpcbData_

> lpData パラメータで指定されたバッファのサイズをバイト数で指定する変数へのポインタです。関数から戻ると、この変数には lpData に保存されたデータのサイズを保存します。

_dwFlags_

> このパラメータは予約されており、0 を指定する必要があります。

## 戻り値

> 成功すると ERROR\_SUCCESS に返します。失敗すると Winerror.h で定義された 0 でないエラー コードに返します。

## バージョン

> EmEditor Version 7.00 以上で利用できます。
