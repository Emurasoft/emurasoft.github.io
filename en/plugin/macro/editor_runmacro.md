# Editor\_RunMacro

Runs a macro. You can use this inline function or explicitly send the [EE\_RUN\_MACRO](../message/ee_run_macro)
message.

Editor\_RunMacro( HWND _hwnd_, UINT _nFlags_, UINT _nDefMacroLang_, LPCWSTR _pszMacroFile_, LPCWSTR _pszText_, const POINT\_PTR\* _pptOrgPos_, POINT\_PTR\* _pptCodePos_, POINT\_PTR\* _pptErrorPos_, HGLOBAL\* _phstrResult_ );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nFlags_

Specifies one of the following values.

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile parameter is valid. |
| RUN\_TEXT | pszText parameter is valid. |

_nDefMacroLang_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | The macro is JScript. |
| MACRO\_LANG\_V8 | The macro is V8. |
| MACRO\_LANG\_VBSCRIPT | The macro is VBScript. |
| MACRO\_LANG\_UNKNOWN | The macro language is unknown. |
| MACRO\_SYNC\_ONLY | Executes the macro synchronously. |

_pszMacroFile_

Specifies the path and file name of the macro file you want to run.

_pszText_

Specifies a macro text on memory that you want to run.

_pptOrgPos_

Specifies the original position of the macro.

_pptCodePos_

Specifies the code position of the macro.

_pptErrorPos_

Receives the error position of the macro.

_phstrResult_

Receives the handle to the output string that the macro returns. The caller is responsible to free this handle by using the GlobalFree function.

## Return Values

The return value is one of the following values.

|     |     |
| --- | --- |
| S\_OK | Success. |
| S\_FALSE | A macro error like a syntax error occurred. |
| S\_EDIT\_TEMP | A macro error occurred but could not open the source code to edit because the source code is not in a text file. The caller should open the source file with the cursor position set according to the information provided by the ptErrorPos parameter. |
| E\_FAIL | A fatal error occurred. |

## Version

Supported on EmEditor Version 9.00 or later.
