# Shell 對象

## 屬性

|     |     |
| --- | --- |
| **[ForegroundWindow](foreground_window)** | 檢索當前置前視窗。 |
| **[KeepRunning](keep_running)** | 檢索或設定標志以在使用 V8 時繼續運行巨集。 |
| **[windows](windows)** | 返回頂層視窗集合。 |

## 方法

|     |     |
| --- | --- |
| [**CreateFolder**](create_folder) | 創建一個資料夾。 |
| [**DeleteFile**](delete_file) | 刪除一個或多個指定的檔案。 |
| [**DeleteFolder**](delete_folder) | 刪除一個或多個指定的資料夾及其內容。 |
| [**FileExists**](file_exists) | 如果指定檔案存在則返回 true；如果沒有，則為 false。 |
| **[FindWindow](find_window)** | 通過一個類名和/或視窗標題查找頂層 Window 對象。 |
| [**FolderExists**](folder_exists) | 如果指定資料夾存在則返回 true；如果沒有，則為 false。 |
| [**GetFileAttributes**](get_file_attributes) | 返回指定檔案或資料夾的屬性。 |
| [**Run**](run) | 在新進程中運行程式。 |
| **[SendKeys](send_keys)** | 發送一個或多個鍵擊（或滑鼠活動）到活動視窗中。 |
| [**SetFileAttributes**](set_file_attributes) | 設定指定檔案或資料夾的屬性。 |

## 版本

支持 EmEditor 7.00 或之後的版本。


```{toctree}
:hidden:
:maxdepth: 1
create_folder
delete_file
delete_folder
file_exists
find_window
folder_exists
foreground_window
get_file_attributes
run
send_keys
set_file_attributes
windows
```
