# 创建一个快捷方式 (教程)

要创建一个快捷方式，用 WshShell 对象的 CreateShortcut 方法。

下面的示例代码在桌面上创建一个已打开的文件的快捷方式。

## 

### \[JavaScript (JScript)\]

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

## 参考

)
