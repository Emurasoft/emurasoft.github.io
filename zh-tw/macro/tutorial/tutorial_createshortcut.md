# 創建一個捷徑 (�е{)

要創建一個捷徑，用 WshShell 對象的 CreateShortcut 方法。

下面的示例代碼在桌面上創建一個已打開的檔案的捷徑。

#### \[JavaScript (JScript)\]

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

#### \[VBScript\]

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

## 參考

)
