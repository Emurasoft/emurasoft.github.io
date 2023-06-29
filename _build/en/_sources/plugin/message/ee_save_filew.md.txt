# EE\_SAVE\_FILEW

Saves the text to a specified file. The file name is specified by an ANSI
string. You can send this message explicitly or use the
[Editor\_SaveFileW](../macro/editor_savefilew) inline function.

EE\_SAVE\_FILEW

wParam = (WPARAM) (BOOL) bReplace;

lParam = (LPARAM) (LPWSTR) szFileName;

## Parameters

_bReplace_

> Specifies TRUE if the text will be saved as by a specified name, and the
> file name EmEditor holds and the title shown on the EmEditor Window will be
> changed. Specifies FALSE if the copy of the text is saved, and the file name
> EmEditor holds will not be changed.

_szFileName_

> Specifies a full path file name in bytes.

## Return Values

> If it is succeeded, the return value is nonzero. If it isn't succeeded, the
> return value is zero.