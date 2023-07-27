# Editor\_SaveFileA

Saves the text to a specified file. The file name is specified as an ANSI
string. You can use this inline function or explicitly send the
[EE\_SAVE\_FILEA](../message/ee_save_filea) message.

Editor\_SaveFileA( HWND hwnd, BOOL bReplace, LPSTR szFileName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_bReplace_

Specifies TRUE if the text will be saved under a specified name; the
file name EmEditor holds and the title shown on the EmEditor Window will be
changed. Specifies FALSE if a copy of the text is saved; the file name
EmEditor holds will not be changed.

_szFileName_

Specifies a full path file name in bytes.

## Return Values

If it is succeeded, the return value is nonzero. If it isn't succeeded, the
return value is zero.
