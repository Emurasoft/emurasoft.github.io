# ExtractColumns 方法

抽出 CSV 文檔中的指定欄。

#### \[JavaScript\]

document. **ExtractColumns**( _strColumns_ );

#### \[VBScript\]

document. **ExtractColumns** _strColumns_

## 參數

_strColumns_

指定要包含在輸出文檔中的欄的字串。此值是以逗號分隔的欄的組合。每欄可以是欄的第一行，也可以是冒號（：）后跟欄的索引。 例如，「:1, :3」將輸出活動文檔的第一欄和第三欄。另外，「姓，名」將輸出第一行與「姓」或「名」符合的欄。

## 版本

支持 EmEditor Professional 18.4 或之後的版本。