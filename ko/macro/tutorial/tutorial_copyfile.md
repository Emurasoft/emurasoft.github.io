# 파일 복사 (Ʃ�丮��)

파일을 복사하려면 FileSystem 개체의 CopyFile 메서드를 사용합니다.

다음의 예제 코드는 열린 파일의 백업을 생성합니다.

## 

### \[JavaScript\]

```
if( document.FullName == '' ){
alert( "The file is untitled." );
}
else {
fso = new ActiveXObject( "Scripting.FileSystemObject" );
fso.CopyFile( document.FullName, document.FullName + ".bak"
);
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

## 참조:
