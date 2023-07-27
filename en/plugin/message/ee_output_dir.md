# EE\_OUTPUT\_DIR

Sets the current directory for the output bar. You can send this
message explicitly or use the [Editor\_OutputDir](../macro/editor_outputdir) inline function.

EE\_OUTPUT\_DIR

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szCurrDir;

## Parameters

_szCurrDir_

Specifies the current directory. This information is necessary if the text contains a clickable relative path that can be jumped only from the current directory.

## Return Values

The return value is not used.

## Version

Supported on EmEditor Version 7.00 or later.
