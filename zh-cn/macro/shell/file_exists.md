# FileExists 方法 (Shell ����)

如果指定文件存在则返回 true；如果没有，则为 false。

#### \[JavaScript\]

b = shell. **FileExists**( _strFile_ );

#### \[VBScript\]

b = shell. **FileExists**( _strFile_ )

## 参数

_strFile_

要确定其存在的文件的名称。

## 示例

#### \[JavaScript\]

b = shell.FileExists( "C:\\\Test\\\file.txt" );

#### \[VBScript\]

b = shell.FileExists( "C:\\Test\\file.txt" )

## 版本

支持 EmEditor Professional 22.1 或之后的版本。