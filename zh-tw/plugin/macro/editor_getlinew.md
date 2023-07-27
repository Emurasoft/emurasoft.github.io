# Editor\_GetLineW

檢索指定行的 Unicode 文字。您能直接用該內嵌函式或明確地發送
[EE\_GET\_LINEW](../message/ee_get_linew) 消息。

Editor\_GetLineW( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPWSTR szString );

Editor\_GetLineW( HWND hwnd, HEEDOC hDoc, UINT\_PTR yLine, LPWSTR pBuf, UINT\_PTR cchBuf, UINT flags, BYTE byteCrLf )

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pGetLineInfo_

指標至 [GET\_LINE\_INFO](../structure/get_line_info) 結構。

_szString_

指標至會接收文字的緩沖區。

_hDoc_

指定目標文件的控點。

_yLine_

指定要檢索的文字的行號。

_pBuf_

指針指向將接收文字的緩沖區。

_cchBuf_

指定要複製到由 _pBuf_ 參數指定的緩沖區的最大字元數。如果指定 0，則返回值是可以接收文字的緩沖區所需的大小（以字元為單位）。

_flags_

該參數的低字是以下值的組合。

|     |     |
| --- | --- |
| FLAG\_LOGICAL | 通過邏輯座標 _yLine_ 指定 _yLine_ 欄位。 |
| FLAG\_WITH\_CRLF | 在文字中添加返回碼。 |
| FLAG\_GET\_CRLF\_BYTE | 指示 _byteCrLf_ 欄位用顯示換行符號的旗標填充。還必須指定 FLAG\_LOGICAL。 |

該參數的高字為目標文件的索引。應在旗標的較高字處指定從 1 開始的索引。如果在旗標的較高字處指定 0，則目前使用中的文件將成為目標。

_byteCrLf_

接收顯示指定行的換行符號的旗標。只有在 _flags_ 參數中同時指定了 FLAG\_LOGICAL 和 FLAG\_GET\_CRLF\_BYTE 時才使用此欄位。它將是以下值之一。

|     |     |
| --- | --- |
| 0 | CR+LF 或檔案結尾。 |
| FLAG\_CR\_ONLY | 僅 CR。 |
| FLAG\_LF\_ONLY | 僅 LF。 |

## 返回值

如果 _cchBuf_ 為零，則返回值是以字元為單位的，可以接收文字的緩沖區所需的大小。如果 _cchBuf_ 非零，則不使用返回值。
