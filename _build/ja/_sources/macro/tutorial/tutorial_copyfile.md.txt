# ファイルをコピーする

ファイルをコピーするには、WshShell オブジェクトの FileSystemObject メソッドを利用することができます。

この例では、開いているファイルのバックアップを作成します。

#### \[JavaScript (JScript)\]

if( document.FullName == '' ){

alert( "The file is untitled." );

}

else {

fso = new ActiveXObject( "Scripting.FileSystemObject" );

fso.CopyFile( document.FullName, document.FullName + ".bak"
);

}

#### \[VBScript\]

If document.FullName = "" Then

alert "The file is untitled."

Else

Set fso = CreateObject( "Scripting.FileSystemObject" )

fso.CopyFile document.FullName, document.FullName + ".bak"

End If

## 参考

)