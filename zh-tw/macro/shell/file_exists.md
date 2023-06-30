# FileExists 方法 (Shell ��H)

如果指定檔案存在則返回 true；如果沒有，則為 false。

#### \[JavaScript\]

b = shell. **FileExists**( _strFile_ );

#### \[VBScript\]

b = shell. **FileExists**( _strFile_ )

## 參數

_strFile_

要確定其存在的檔案的名稱。

## 範例

#### \[JavaScript\]

b = shell.FileExists( "C:\\\Test\\\file.txt" );

#### \[VBScript\]

b = shell.FileExists( "C:\\Test\\file.txt" )

## 版本

支持 EmEditor Professional 22.1 或之後的版本。