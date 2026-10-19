# GetFastViewDiffPath 方法 (Editor 对象)

检索指定文件的快速查看模式差异文件的路径。

## 

### \[JavaScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile );
```

### \[VBScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile )
```

## 参数

_strFile_

指定文件的路径。

## 返回值

返回用于保存该文件在快速查看模式下的编辑内容和行的位置的差异文件的路径。如果找不到该文件的差异文件，则返回 [**保存差异** 命令](../../cmd/file/fast_view_save_diff) 将要保存差异文件的路径，因此返回的文件可能不存在。

## 备注

差异文件保存在 EmEditor 本地应用程序数据文件夹中的 **FastView** 文件夹中。详细信息请参见[以快速查看模式打开和编辑超大文件](../../howto/file/file_fast_view)。

## 示例

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
