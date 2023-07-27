# InsertFromFile 方法 (Selection ����)

在光标位置处插入指定文件的内容。

## 

### \[JavaScript\]

```
document.selection.InsertFromFile( strFileName, nEncoding, nFlags );
```

### \[VBScript\]

```
document.selection.InsertFromFile strFileName, nEncoding, nFlags
strFileName
指定要打开的文件的完整路径以及名称。
nEncoding
从[编码常数](../const/constencoding) 中选择或指定任何用于 Windows 操作系统的代码页。
nFlags
指定一个下列值的组合:
|     |     |
| --- | --- |
| eeOpenDetectUnicode | 检测 Unicode 签名 (BOM)。 |
| eeOpenDetectUTF8 | 检测 UTF-8。 |
| eeOpenDetectCharset | 检测 HTML/XML 字符集。 |
| eeOpenDetectAll | 检测所有编码。 |
```

## 版本

支持 EmEditor 4.00 或之后的版本。
