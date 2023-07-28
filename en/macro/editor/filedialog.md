# FileDialog Method (Editor Object)

Displays an Open or Save As dialog box that lets the user specify the drive,
directory, and the name of a file to open.

## 

### \[JavaScript\]

```
strFileName = editor.FileDialog( nType [, nFlags [, strTitle [, strFilter [, nDefFilterIndex [, strDefPath [, strDefFolder [, strDefExt ]]]]]]] );
```

### \[VBScript\]

```
strFileName = editor.FileDialog( nType [, nFlags [, strTitle [, strFilter [, nDefFilterIndex [, strDefPath [, strDefFolder [, strDefExt ]]]]]]] )
```

## Parameters

_nType_

Specifies one of the following values.

|     |     |
| --- | --- |
| eeFileDialogOpen | Creates an Open dialog box. |
| eeFileDialogSaveAs | Creates a Save As dialog box. |

_nFlags_

Optional. Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeFileDialogCreatePrompt | If the user specifies a file that does not exist, this flag causes the dialog box to prompt the user for permission to create the file. |
| eeFileDialogDontAddToRecent | Prevents the system from adding a link to the selected file in the file system directory that contains the user's most recently used documents. |
| eeFileDialogFileMustExist | Specifies that the user can type only names of existing files in the **File Name** entry field. If this flag is specified and the user enters an invalid name, the dialog box procedure displays a warning in a message box. If this flag is specified, the <br> eeFileDialogPathMustExist flag is also used. |
| eeFileDialogNoChangeDir | Restores the current directory to its original value if the user changed the directory while searching for files. |
| eeFileDialogNoDereferenceLinks | Directs the dialog box to return the path and file name of the selected shortcut (.LNK) file. If this value is not specified, the dialog box returns the path and file name of the file referenced by the shortcut. |
| eeFileDialogNoNetworkButton | Hides and disables the **Network** button. |
| eeFileDialogNoReadOnlyReturn | Specifies that the returned file does not have the **Read Only** check box selected and is not in a write-protected directory. |
| eeFileDialogNoTestFileCreate | Specifies that the file is not created before the dialog box is closed. |
| eeFileDialogNoValidate | Specifies that the common dialog boxes allow invalid characters in the returned file name. |
| eeFileDialogOverwritePrompt | Causes the **Save As** dialog box to generate a message box if the selected file already exists. |
| eeFileDialogPathMustExist | Specifies that the user can type only valid paths and file names. |
| eeFileDialogShareAware | Specifies that if the function fails because of a network sharing violation, the error is ignored and the dialog box returns the selected file name. |

_strTitle_

Optional. Specifies the title of the dialog box. If this is an empty string, the
default title ( **Open** or **Save As**) is used.

_strFilter_

Optional. Specifies the filter. The string must be in the following format:

"Text Files\|\*.txt\|All Files\|\*.\*\|\|"

If this is an empty string, no filter is used.

_nDefFilterIndex_

Optional. Specifies the one-base index of the initially selected filter.

_strDefPath_

Optional. Specifies the initially selected path.

_strDefFolder_

Optional. Specifies the initially selected folder.

_strDefExt_

Optional. Specifies the default file extension.

## Return Values

Returns the full path and name of the selected file when successful. Returns an empty string if the user selects the **Cancel** button.

## Version

Supported on EmEditor Professional Version 8.00 or later.
