# 操作注册表 (教程)

要操作注册表，用 RegRead 方法，RegWrite 方法，和 WshShell 对象 的 RegDelete 方法。

下面的示例代码会从注册表上读取一个运行的宏的文件名称，并显示它。

## 

### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

str = WshShell.RegRead( "HKCU\\\Software\\\EmSoft\\\EmEditor v3\\\Common\\\MacroFile"
);

alert( str );

### \[VBScript\]

```
Set WshShell = CreateObject( "WScript.Shell" )
str = WshShell.RegRead( "HKCU\\Software\\EmSoft\\EmEditor v3\\Common\\MacroFile" )
alert str
```

## 提示:

在 JavaScript 中，如果你想要在一个字符串中包括一个反斜杠 "\\"，它必须在前面加上另一个反斜杠 "\\\"。

## 参考

)
