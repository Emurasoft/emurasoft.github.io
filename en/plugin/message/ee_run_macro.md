# EE\_RUN\_MACRO

Runs a macro. You can send this message explicitly or by using the [Editor\_RunMacro](../macro/editor_runmacro)
inline function.

EE\_RUN\_MACRO

wParam = 0;

lParam = (LPARAM) (RUN\_MACRO\_INFO\*) pRMI;

## Parameters

_pRMI_

Pointer to the [RUN\_MACRO\_INFO](../structure/run_macro_info) structure.

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
