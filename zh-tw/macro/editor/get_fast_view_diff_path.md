# GetFastViewDiffPath 方法 (Editor 對象)

檢索指定檔案的快速檢視模式差異檔路徑。

## 

### \[JavaScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile );
```

### \[VBScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile )
```

## 參數

_strFile_

指定檔案的路徑。

## 返回值

返回儲存該檔案在快速檢視模式中的編輯內容和行位置的差異檔路徑。如果找不到該檔案的差異檔，則返回 [**儲存差異** 命令](../../cmd/file/fast_view_save_diff) 將會儲存差異檔的路徑，因此返回的檔案可能不存在。

## 備註

差異檔儲存在 EmEditor 本機應用程式資料資料夾的 **FastView** 資料夾中。詳細資訊請參見[在快速檢視模式中開啟和編輯巨型檔案](../../howto/file/file_fast_view)。

## 範例

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

## 版本

支持 EmEditor Professional 26.4 或更高版本。
