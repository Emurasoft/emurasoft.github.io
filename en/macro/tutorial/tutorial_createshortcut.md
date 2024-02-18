# Create a Shortcut (Tutorial)

To create a shortcut, use the CreateShortcut Method of a WshShell Object.

The following example code creates a shortcut on the desktop to an opened file.

## 

### \[JavaScript (JScript)\]

```
if( document.FullName == "" ) {
    alert( "The file is untitled." );
}
else {
    WshShell = new ActiveXObject( "WScript.Shell" );
    strDesktop = WshShell.SpecialFolders("Desktop");
    oShellLink = WshShell.CreateShortcut(strDesktop + "\\\\Shortcut to My File.lnk");
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

## References

[Microsoft MSDN Library: CreateShortcut Method](https://docs.microsoft.com/en-us/previous-versions//xsy6k3ys(v=vs.85))
