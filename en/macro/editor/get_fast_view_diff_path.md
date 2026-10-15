# GetFastViewDiffPath Method (Editor Object)

Retrieves the path of the diff file of Fast View mode for the specified file.

## 

### \[JavaScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile );
```

### \[VBScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile )
```

## Parameters

_strFile_

Specifies the path of the file.

## Return Values

Returns the path of the diff file that stores the edits and the line positions of the file in Fast View mode. If no diff file is found for the file, returns the path where the [**Save Diff** command](../../cmd/file/fast_view_save_diff) would save the diff file, so the returned file might not exist.

## Remarks

Diff files are saved in the **FastView** folder in the local application data folder of EmEditor. See [To Open and Edit Huge Files in Fast View Mode](../../howto/file/file_fast_view) for details.

## Examples

### \[JavaScript\]

```
sDiff = editor.GetFastViewDiffPath( document.FullName );
fso = new ActiveXObject( "Scripting.FileSystemObject" );
if( fso.FileExists( sDiff ) )  alert( "The diff file exists: " + sDiff );
```

### \[VBScript\]

```
sDiff = editor.GetFastViewDiffPath( document.FullName )
Set fso = CreateObject( "Scripting.FileSystemObject" )
If fso.FileExists( sDiff ) Then alert( "The diff file exists: " & sDiff )
```

## Version

Supported on EmEditor Professional Version 26.4 or later.
