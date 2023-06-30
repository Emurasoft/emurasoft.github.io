# GetFileAttributes 方法 (Shell ����)

返回指定文件或文件夹的属性。

#### \[JavaScript\]

nAttr = shell. **GetFileAttributes**( _strFile_ );

#### \[VBScript\]

nAttr = shell. **GetFileAttributes**( _strFile_ )

## 参数

_strFile_

用于检索属性的文件或文件夹的完整路径和名称。

## 示例

#### \[JavaScript\]

nAttr = shell.GetFileAttributes( "C:\\\Test\\\file.txt" );

#### \[VBScript\]

nAttr = shell.GetFileAttributes( "C:\\Test\\file.txt" )

## 返回值

返回以下值的组合。

|     |     |
| --- | --- |
| 值 | 描述 |
| 0 | 正常 |
| 1 | 只读 |
| 2 | 隐藏 |
| 4 | 系统 |
| 8 | 数量 |
| 16 | 目录 |
| 32 | 存档 |
| 1024 | 别名 |
| 2048 | 已压缩 |

## 版本

支持 EmEditor Professional 22.1 或之后的版本。