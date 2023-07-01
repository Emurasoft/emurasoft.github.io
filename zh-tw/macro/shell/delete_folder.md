# DeleteFolder 方法 (Shell ��H)

刪除一個或多個指定的資料夾及其內容。指定的資料夾即使不為空也會被刪除。

#### \[JavaScript\]

shell. **DeleteFolder**( _strFolder_ );

#### \[VBScript\]

shell. **DeleteFolder** _strFolder_

## 參數

_strFolder_

要刪除的資料夾的名稱。它可以在最後一個路徑組件中包含通配符。

## 範例

#### \[JavaScript\]

shell.DeleteFolder( "C:\\\Test\\\folder" );

#### \[VBScript\]

shell.DeleteFolder "C:\\Test\\folder"

## 版本

支持 EmEditor Professional 22.1 或之後的版本。
