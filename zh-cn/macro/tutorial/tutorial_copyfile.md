# 复制一个文件 (教程)

要复制一个文件，用 FileSystemObject 中的 CopyFile 方法。

下面的示例代码会创建一个打开文件的备份。

## 

### \[JavaScript (JScript)\]

```
if( document.FullName == '' ){
    alert( "The file is untitled." );
}
else {
    fso = new ActiveXObject( "Scripting.FileSystemObject" );
    fso.CopyFile( document.FullName, document.FullName + ".bak" );
}
```

### \[VBScript\]

```
If document.FullName = "" Then
alert "The file is untitled."
Else
Set fso = CreateObject( "Scripting.FileSystemObject" )
fso.CopyFile document.FullName, document.FullName + ".bak"
End If
```

## 参考

[Microsoft MSDN Library: CopyFile Method](https://docs.microsoft.com/en-us/previous-versions//e1wf9e7w(v=vs.85))
