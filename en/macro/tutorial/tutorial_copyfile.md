# Copy a File (Tutorial)

To copy a file, CopyFile Method of a FileSystemObject.

The following example code creates a backup of an open file.

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

## References

)
