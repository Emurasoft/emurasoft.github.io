# Editor\_RunMacro

運行一個巨集。您能直接用該內嵌函式或明確地發送 [EE\_RUN\_MACRO](../message/ee_run_macro)
消息。

Editor\_RunMacro( HWND _hwnd_, UINT _nFlags_, UINT _nDefMacroLang_, LPCWSTR _pszMacroFile_, LPCWSTR _pszText_, POINT\_PTR\* _pptOrgPos_, POINT\_PTR\* _pptCodePos_, POINT\_PTR\* _pptErrorPos_, HGLOBAL\* _phstrResult_ );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nFlags_

指定下列值之一。

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile 參數有效。 |
| RUN\_TEXT | pszText parameter 參數有效。 |

_nDefMacroLang_

指定下列值的組合。

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | 該巨集是 JScript。 |
| MACRO\_LANG\_V8 | 該巨集是 V8。 |
| MACRO\_LANG\_VBSCRIPT | 該巨集是 VBScript。 |
| MACRO\_LANG\_UNKNOWN | 該巨集語言未知。 |
| MACRO\_SYNC\_ONLY | 同步執行巨集。 |

_pszMacroFile_

指定您想要運行的巨集檔案的路徑以及名稱。

_pszText_

在內存上指定您想要運行的一段巨集文字。

_pptOrgPos_

指定巨集的原始位置。

_pptCodePos_

指定巨集的代碼位置。

_pptErrorPos_

接收巨集的錯誤位置。

_phstrResult_

接收句柄來輸出巨集返回的字串。調用方負責使用 GlobalFree 函數來釋放該句柄。

## 返回值

返回值是下列值之一。

|     |     |
| --- | --- |
| S\_OK | 成功。 |
| S\_FALSE | 存在一個巨集錯誤，如語法錯誤。 |
| S\_EDIT\_TEMP | 存在一個巨集錯誤，但無法打開源代碼來編輯因為源代碼不是一個文字檔案。調用方應當用被按照 ptErrorPos 參數提供的信息設置的游標位置來打開源檔案。 |
| E\_FAIL | 存在一個嚴重錯誤。 |

## 支持版本

支持 EmEditor 9.00 或之後的版本。
