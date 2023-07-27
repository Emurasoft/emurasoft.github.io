# 바로가기 생성 (Ʃ�丮��)

바로가기를 생성하려면 WshShell 개체의 CreateShortcut 메서드를 사용합니다.

다음의 예제 코드는 바탕 화면에 열려져 있는 파일의 바로가기를 생성합니다.

## 

### \[JavaScript\]

```
if( document.FullName == "" ) {
alert( "The file is untitled." );
}
else {
WshShell = new ActiveXObject( "WScript.Shell" );
strDesktop = WshShell.SpecialFolders("Desktop");
oShellLink = WshShell.CreateShortcut(strDesktop + "\\\Shortcut
to My File.lnk");
oShellLink.TargetPath = document.FullName;
oShellLink.WindowStyle = 1;
oShellLink.Description = "Shortcut to My File";
oShellLink.WorkingDirectory = strDesktop;
oShellLink.Save();
}
```

### \[VBScript\]

```
If document.FullName = "" Then
alert "The file is untitled."
Else
Set WshShell = CreateObject( "WScript.Shell" )
strDesktop = WshShell.SpecialFolders("Desktop")
set oShellLink = WshShell.CreateShortcut(strDesktop &
"\\Shortcut to My File.lnk")
oShellLink.TargetPath = document.FullName
oShellLink.WindowStyle = 1
oShellLink.Description = "Shortcut to My File"
oShellLink.WorkingDirectory = strDesktop
oShellLink.Save
End If
```

## 참조:
