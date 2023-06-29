# EE\_SAVE\_FILEA

Saves the text to a specified file. The file name is specified by an ANSI
string. You can send this message explicitly or use the
[Editor\_SaveFileA](../macro/editor_savefilea) inline function.

EE\_SAVE\_FILEA

wParam = (WPARAM) (BOOL) bReplace;

lParam = (LPARAM) (LPSTR) szFileName;

## Parameters

_bReplace_

> Specifies TRUE if the text will be saved by a specified name, and the
> file name EmEditor holds. The title shown on the EmEditor Window will be
> changed. Specifies FALSE if the copy of the text is saved, and the file name
> EmEditor holds will not be changed.

_szFileName_

> Specifies a full path file name in bytes.

## Return Values

> If it is succeeded, the return value is nonzero. If it isn't succeeded, the
> return value is zero.