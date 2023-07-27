# Editor\_DocSaveFileW

Saves the text of the specified document to a specified file. The file name is specified as a Unicode string. You can use this inline function or explicitly send the
[EE\_SAVE\_FILEW](../message/ee_save_filew) message.

Editor\_SaveFileW( HWND hwnd, int iDoc, BOOL bReplace, LPWSTR szFileName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_iDoc_

Specifies the index of the target document. If -1 is specified, the currently active document will be targeted.

_bReplace_

Specifies TRUE if the text will be saved as by a specified name; the
file name EmEditor holds and the title shown on the EmEditor Window will be
changed. Specifies FALSE if the copy of the text is saved; the file name
EmEditor holds will not be changed.

_szFileName_

Specifies a full path file name in bytes.

## Return Values

If it is succeeded, the return value is nonzero. If it isn't succeeded, the
return value is zero.

## Version

Supported on EmEditor Professional Version 5.00 or later.
