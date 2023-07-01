# BatchReplaceInFiles 方法 (Editor ��H)

在多個檔案中取代多個字串。

#### \[JavaScript\]

nFound = editor. **BatchReplaceInFiles**( _filters_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _strBackupPath_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] \] );

#### \[VBScript\]

nFound = editor. **BatchReplaceInFiles**( _filters_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _strBackupPath_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] \] )

## 參數

_filters_

指定包含搜索字串和標志的 [**Filters** 集合](../filters/index)。

_strPath_

指定要搜索的路徑。它可以包括通配符，例如\\* 以及 ?。

_nFlags_

指定一個以下值的組合。

|     |     |
| --- | --- |
| eeFindRecursive | 在指定路徑的子資料夾中搜索。 |
| eeFindReplaceIgnoreFiles | 忽略由 _strFilesToIgnore_ 指定的檔案或資料夾。 |
| eeOpenDetectAll | 檢測所有編碼。 |
| eeOpenDetectCharset | 檢測 HTML/XML 字元集。 |
| eeOpenDetectUnicode | 檢測 Unicode 簽名 (BOM)。 |
| eeOpenDetectUTF8 | 檢測 UTF-8。 |
| eeReplaceBackup | 儲存備份。不能與 eeReplaceKeepOpen 合用。 |
| eeReplaceKeepOpen | 保持修改的檔案為打開狀態。不能與 eeReplaceBackup 合用。 |

_nEncoding_

從 **[編碼常數](../const/const_encoding)** 中選擇或指定任何用於 Windows 操作系統的程式碼頁。如果指定 0 或省略，將使用與搜索的檔案名關聯的組態屬性中指定的編碼。

_strFilesToIgnore_

如果 _nFlags_ 包括 eeFindReplaceIgnoreFiles，指定要忽略的檔案或資料夾名稱。它可以包括通配符，例如 \* 和 ?。要指定多個檔案，用分號 (;) 來隔開檔案。

_strBackupPath_

指定備份資料夾如果 _nFlags_  指定了 eeReplaceBackup。

_nExFlags_

指定以下值的組合。但是，只能指定 eeExFindRegexBoost 和 eeExFindRegexOnigmo 中的一個。如果未指定這兩者，則使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindMulti | 執行 **多項取代全部**。如果未指定，則執行 **批次取代全部**。詳情請參閱 [**批次取代全部和多項取代全部之間的區別**](../../howto/search/batch_vs_bulk)。 |
| eeExFindRegexBoost | 使用 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 使用 Onigmo 作為規則運算式引擎。 |

_nLimit_

當符合數達到此數字時，EmEditor 將停止搜索檔案。 如果指定 0，則 EmEditor 不會停止搜索檔案。

## 返回值

返回值是在所有搜索的檔案中取代的字串總數。

## 備註

除非 _nFlags_  指定 eeReplaceKeepOpen，否則無法復原此操作。
建議將 eeReplaceBackup 指定為 _nFlags_  並儲存備份。
如果備份資料夾中存在相同的檔案名，則新備份將覆蓋舊檔案。

## 版本

支持 EmEditor Professional 20.0 或之後的版本。
