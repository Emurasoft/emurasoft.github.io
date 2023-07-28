# 複製一個檔案 (教程)

要複製一個檔案，用 FileSystemObject 中的 CopyFile 方法。

下面的示例代碼會創建一個打開檔案的備份。

## 

### \[JavaScript (JScript)\]

if( document.FullName == '' ){

alert( "The file is untitled." );

}

else {

fso = new ActiveXObject( "Scripting.FileSystemObject" );

fso.CopyFile( document.FullName, document.FullName + ".bak"
);

}

### \[VBScript\]

```
If document.FullName = "" Then
alert "The file is untitled."
Else
Set fso = CreateObject( "Scripting.FileSystemObject" )
fso.CopyFile document.FullName, document.FullName + ".bak"
End If
```

## 參考

)
