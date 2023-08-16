# RUN\_MACRO\_INFO

Used by [EE\_RUN\_MACRO](../message/ee_run_macro) message.

typedef struct \_RUN\_MACRO\_INFO {

size\_t cbSize;

LPCWSTR pszMacroFile;

LPCWSTR pszText;

UINT nFlags;

int nDefMacroLang;

POINT\_PTR ptOrgPos;

POINT\_PTR ptCodePos;

POINT\_PTR ptErrorPos;

HGLOBAL hstrResult;

} RUN\_MACRO\_INFO;

## Members

_cbSize_

Size of this data structure, in bytes. Set this member to sizeof( RUN\_MACRO\_INFO ) before sending the EE\_RUN\_MACRO message.

_pszMacroFile_

Specifies the path and file name of the macro file you want to run.

_pszText_

Specifies a macro text on memory that you want to run.

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

_ptOrgPos_

Specifies the original position of the macro.

_ptCodePos_

Specifies the code position of the macro.

_ptErrorPos_

Specifies the error position of the macro.

_hstrResult_

Output. Receives the handle to the output string that the macro returns. The caller is responsible to free this handle by using the GlobalFree function.

## Version

Supported on Version 9.00 or later.
