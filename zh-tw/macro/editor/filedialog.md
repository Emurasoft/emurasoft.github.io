# FileDialog 方法 (Editor ��H)

顯示一個「打開」或「另存為」對話方塊，讓用戶指定驅動器、目錄以及要打開的檔案名。

#### \[JavaScript\]

_strFileName_ = editor. **FileDialog**( _nType_ \[, _nFlags_ \[, _strTitle_ \[, _strFilter_ \[, _nDefFilterIndex_ \[, _strDefPath_ \[, _strDefFolder_ \[, _strDefExt_ \]\]\]\]\]\]\] );

#### \[VBScript\]

_strFileName_ = editor. **FileDialog**( _nType_ \[, _nFlags_ \[, _strTitle_ \[, _strFilter_ \[, _nDefFilterIndex_ \[, _strDefPath_ \[, _strDefFolder_ \[, _strDefExt_ \]\]\]\]\]\]\] )

## 參數

_nType_

指定下列值之一:

|     |     |
| --- | --- |
| eeFileDialogOpen | 創建一個「打開」對話方塊。 |
| eeFileDialogSaveAs | 創建一個「另存為」對話方塊。 |

_nFlags_

可選項。指定一個下列對話方塊的組合。

|     |     |
| --- | --- |
| eeFileDialogCreatePrompt | 如果用戶指定一個不存在的檔案，這個標志會彈出一個對話方塊提示用戶是否允許創建該檔案。 |
| eeFileDialogDontAddToRecent | 防止系統添加一個連結到檔案系統目錄上被選取的檔案中，該檔案系統目錄包含用戶最近使用的文檔。 |
| eeFileDialogFileMustExist | 指定用戶只能輸入已存在檔案的檔案名在 **檔案名** 輸入欄位。如果指定了該標志而用戶輸入了一個無效的名稱，對話方塊會顯示一條警告消息。如果指定了該標志，eeFileDialogPathMustExist 也會被用到。 |
| eeFileDialogNoChangeDir | 把當前目錄還原到它初始值如果用戶在搜尋檔案時更改了該目錄。 |
| eeFileDialogNoDereferenceLinks | 引導對話方塊返回所選擇的快捷方式 (.LNK) 檔案的路徑和檔案名。若不指定任何值，則對話方塊返回由該快捷方式引用的檔案的路徑和檔案名。 |
| eeFileDialogNoNetworkButton | 隱藏并禁用 **「Network」** 按鈕。 |
| eeFileDialogNoReadOnlyReturn | 指定被返回的檔案沒有 **只讀** 復選框并且不在寫保護目錄中。 |
| eeFileDialogNoTestFileCreate | 指定在對話方塊關閉之前不創建檔案。 |
| eeFileDialogNoValidate | 指定常用對話方塊允許無效字符在被返回的檔案名中。 |
| eeFileDialogOverwritePrompt | 讓 **另存為** 對話方塊產生一個消息框如果被選取的檔案已存在。 |
| eeFileDialogPathMustExist | 指定用戶能輸入僅有效的路徑以及檔案名。 |
| eeFileDialogShareAware | 指定如果由于網絡共享沖突導致函數失敗，忽略錯誤并且對話方塊會返回選擇的檔案名。 |

_strTitle_

可選項。指定對話方塊的標題。如果這是一個空的字符串，會使用預設的標題 ( **打開** 或 **另存為**) 。

_strFilter_

可選項。指定過濾器。字符串必須是以下格式:

"Text Files\|\*.txt\|All Files\|\*.\*\|\|"

如果這是一個空字符串，不使用過濾器。

_nDefFilterIndex_

可選項。指定最初選擇的過濾器的以 1 為基準的索引。

_strDefPath_

可選項。指定最初選擇的路徑。

_strDefFolder_

可選項。指定最初選擇的資料夾。

_strDefExt_

可選項。指定預設檔案擴展名。

## 返回值

如果成功，返回被選取檔案的完整路徑以及名稱。返回一個空字符串如果用戶選擇了 **「Cancel」** 按鈕。

## 版本

支持 EmEditor 8.00 或之後的版本。
