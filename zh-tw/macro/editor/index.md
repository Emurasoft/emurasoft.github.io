# Editor 對象

## 屬性

|     |     |
| --- | --- |
| **[ActiveDocument](editor_activedocument)** | 為目前的文檔，檢索 Document 對象。 |
| **[Configs](configs)** | 檢索 Configs 集合。 |
| **[CsvList](csv_list)** | 檢索或設置 CsvList 集合。 |
| **[Documents](editor_documents)** | 為目前的打開的文檔，檢索 Documents 集合。 |
| **[EnableTab](editor_enabletab)** | 設置或檢索是否標籤頁被啟用。 |
| **[filters](filters)** | 檢索 Filters 集合。 |
| **[FullName](editor_fullname)** | 檢索 EmEditor 可執行檔案 (emeditor.exe) 的完整規格，包括路徑。 |
| **[FuzzyOptions](fuzzy_options)** | 檢索 FuzzyOptions對象。 |
| **[LangID](langid)** | 檢索目前選取的語言 ID。 |
| **[regex](regex)** | 檢索 Regex 對象。 |
| **[RegisteredName](registeredname)** | 檢索註冊名。 |
| **[Version](editor_version)** | 檢索 表示目前的 EmEditor 版本的字串。 |

## 方法

|     |     |
| --- | --- |
| **[BatchFindInFiles](editor_batchfindinfiles)** | 在多個檔案中搜索多個字串。 |
| **[BatchReplaceInFiles](editor_batchreplaceinfiles)** | 在多個檔案中取代多個字串。 |
| **[Compare](compare)** | 比較兩個文檔。 |
| **[GetUnicodeName](getunicodename)** | 檢索指定字元或字串的 Unicode 名。 |
| **[ExecuteCommandByID](editor_executecommandbyid)** | 執行由一個表示命令 ID 整數標識的命令。 |
| **[ExecuteMacro](editor_executemacro)** | 執行一個指定的巨集。 |
| **[ExecutePlugin](editor_executeplugin)** | 執行指定外掛程式。 |
| **[FileDialog](filedialog)** | 顯示一個「打開」或「另存新檔」對話方塊，讓使用者指定磁碟機、目錄以及要打開的檔案名。 |
| **[FindInFiles](editor_findinfiles)** | 在多個檔案中搜尋符合的字串。 |
| [**GetProfileInt**](getprofileint) | 按 EmEidtor 的設定，從註冊表或一個 INI 檔案上檢索指定項目的整數值。 |
| [**GetProfileString**](getprofilestring) | 按 EmEidtor 的設定，從註冊表或一個 INI 檔案上檢索指定項目的字串值。 |
| [**Join**](join) | 按指定索引鍵資料欄，用一個與 JOIN 操作類似的方法合併兩個 CSV 文檔，並創建一個新文檔。 |
| **[NewFile](editor_newfile)** | 新增一個檔案。 |
| **[OpenFile](editor_openfile)** | 打開一個已存在的檔案。 |
| **[QueryStatusByID](editor_querystatusbyid)** | 檢索指定命令的目前的狀態，是否已被勾選和啟用。 |
| **[QueryStringByID](editor_querystringbyid)** | 檢索與指定命令相關聯的字串。 |
| **[RefreshCommonSettings](refresh_common_settings)** | 加載常用設置並重新整理 EmEditor 視窗。 |
| **[ReplaceInFiles](editor_replaceinfiles)** | 在多個檔案中取代文字。 |
| **[SaveAll](editor_saveall)** | 儲存所有目前的打開的檔案。 |
| **[SaveCloseAll](editor_savecloseall)** | 儲存並關閉所有打開的檔案。 |
| **[Stderr](stderr)** | 將字串寫入標準錯誤。 |
| [**WriteProfileInt**](writeprofileint) | 按 EmEditor 的設定，把一個整數值設置到註冊表或一個 INI 檔案中。 |
| [**WriteProfileString**](writeprofilestring) | 按 EmEditor 的設定，把一個字串值設置到註冊表或一個 INI 檔案中。 |

## 版本

支持 EmEditor 4.00 或之後的版本。


```{toctree}
:maxdepth: 1
compare
configs
csv_list
editor_activedocument
editor_batchfindinfiles
editor_batchreplaceinfiles
editor_documents
editor_enabletab
editor_executecommandbyid
editor_executemacro
editor_executeplugin
editor_findinfiles
editor_fullname
editor_newfile
editor_openfile
editor_querystatusbyid
editor_querystringbyid
editor_replaceinfiles
editor_saveall
editor_savecloseall
editor_version
filedialog
filters
fuzzy_options
getprofileint
getprofilestring
getunicodename
join
langid
refresh_common_settings
regex
registeredname
stderr
writeprofileint
writeprofilestring
```
