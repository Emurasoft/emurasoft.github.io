# OpenFile 方法 (Editor 对象)

打开一个已存在的文件。

## 

### \[JavaScript\]

```
editor.OpenFile( strFileName[, nEncoding[, nFlags]] );
```

### \[VBScript\]

```
editor.OpenFile strFileName[, nEncoding[, nFlags]]
```

## 参数

_strFileName_

指定要打开的文件的完整路径和名称。

_nEncoding_

从 **[编码常数](../const/const_encoding)** 中选择或指定任一用于 Windows 操作系统的编码。如果 0 被指定或省略，这个方法会用属性预设的编码打开文件。

_nFlags_

指定一个下列值的组合。 如 nEncoding 是 0 或被省略，所有除了 eeOpenAllowNewWindow 的值会被忽略。

|     |     |
| --- | --- |
| eeOpenAllowNewWindow | 如果当前文档被命名或修改，把文档作为一个新窗口打开。 |
| eeOpenDetectUnicode | 检测 Unicode 签名 (BOM)。 |
| eeOpenDetectUTF8 | 检测 UTF-8。 |
| eeOpenDetectCharset | 检测 HTML/XML 字符集。 |
| eeOpenDetectAll | 检测所有编码。 |
| eeUseDiskMode | 打开文件时使用启用硬盘的模式。 |
| eeDontUseDiskMode | 打开文件时不使用启用硬盘的模式。如果既没有指定 eeUseDiskMode 也没有指定 eeDontUseDiskMode，EmEditor 会根据要打开的文件大小自动选择使用启用硬盘的模式。 |

## 版本

支持 EmEditor 4.00 或之后的版本。但是，nEncoding 和 nFlags 参数能在 5.00 或之后的版本上被省略。
