# 使用命令列選項

命令列選項能在「開始」功能表中的「運行」對話方塊中或一個命令提示符視窗中被指定。

## 語法

### 打開一個或多個檔案

```
"File1" "File2" "File3" ... [/r] [/fh] [/nr] [/sp] [/l LineNumber] [/cl ColumnNumber] [/cp encoding] [/c "Config"] [/mf "MacroPath"]
```

### 新增一個檔案

```
[/i] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 新增一個檔案並貼上

```
[/i] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 新增一個檔案並貼為引文

```
[/iq] [/i] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 新增一個檔案，貼為引文並換行

```
[/iqr] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 顯示系統匣圖示

```
/ti
```

### 列印一個檔案

```
"File" /p [/nr] [/sp] [/cp encoding]
```

### 比較兩個檔案

```
/cmp "File1" "File2"
```

### 轉換一個檔案編碼

```
"SrcFile" [/nr] [/sp] [/cp EncodingToOpen] [/c "Config"] /cps EncodingToSave /ss+ /sa "DestFile"
```

如果不用 Unicode 簽名 (BOM) 儲存，用 /ss- 而不是 /ss+.

### 顯示「多檔尋找」對話方塊

```
/fd
```

### 顯示「多檔取代」對話方塊

```
/rd
```

### 多檔尋找

```
/fc "FindWhat" [/fr] [/fw] [/x] [/fn] [/fu "FilesToIgnore"] [/cp encoding] "path"
```

當點擊在「多檔尋找」對話方塊中的「尋找」按鈕時，該命令被內部調用。要進行不區分大小的搜尋，用 /fi 而不是 /fc。

### 多檔取代

```
/fc "FindWhat" [/fr] [/fw] [/x] [/ko] [/fu "FilesToIgnore"] [/cp encoding] "path" /rw "ReplaceWith" [/bk "BackupFolder"]
```

當點擊在「多檔取代」對話方塊中的「取代全部」按鈕時，該命令被內部調用。要進行不區分大小的搜尋，用 /fi 而不是 /fc。/ko 和 /bk 不能同時被指定。

### 打開一個檔案並取代

```
"File" /rc "FindWhat" [/fw] [/x] [/cp encoding] /rw "ReplaceWith"
```

當執行「多檔取代」命令時，該命令被內部調用。要進行不區分大小的搜尋，用 /ri 而不是 /rc。

### 還原工作區

```
/ws
```

該命令被內部調用當選擇「還原工作區」命令時。

### 儲存工作區

```
/wss
```

該命令被內部調用當選擇「儲存工作區」命令時。

### 用 EmEditor 抓取文字

```
/eh
```

該命令從系統匣圖示上被調用，當按下在「自訂系統匣圖示」對話方塊中定義的用 EmEditor 抓取文字的快速鍵時。

### 顯示「說明」

```
/?
```

## 選項

|     |     |
| --- | --- |
| `/?` | 顯示「說明」。 |
| `/act` | 激活 EmEditor 如果它已經在運行，或啟動 EmEditor，如果它還沒有運行。 |
| `/bk "BackupFolder"` | 指定一個備份資料夾當多檔取代時。 |
| `/c "Config"` | 設定組態。 |
| `/ca` | 關閉所有文檔。 |
| `/car` | 關閉所有文檔包括隱藏的視窗如果 "快速開始" 選項被啟用。 |
| `/cd` | 在「打開」文字方塊中把目前的目錄設為預設資料夾。 |
| `/cjl` | 自訂在 Windows 7 或之後版本中的跳轉清單。 |
| `/cl ColumnNumber` | 邏輯欄號。負數表示從行尾開始的字元數。 |
| `/clw` | 清除工作去。 |
| `/cmp` | 比較兩個檔案。 |
| `/cp Encoding` | 設定一個用來打開的編碼。一個編碼可以是 [編碼常數](../../macro/const/const_encoding) 之一。可以指定帶有下列數值的組合。<br><table><tr><td>`131072`</td><td>偵測 Unicode 簽名 (BOM)。</td></tr><tr><td>`262144`</td><td>偵測 UTF-8。</td></tr><tr><td>`524288`</td><td>偵測 HTML/XML 字元集。</td></tr><tr><td>`1048576`</td><td>偵測所有編碼。</td></tr></table> |
| `/cps Encoding` | 設定一個用來打開的編碼。一個編碼可以是 [編碼常數](../../macro/const/const_encoding) 之一。 |
| `/csv "CSVName"` | 設定初始 CSV 模式，停用 CSV 檢測。 _CSVName_ 可以是 CSV 格式的名稱或索引號。如果指定為 0，則使用普通模式。 |
| `/di "Folder"` | 指定工作資料夾當創建一個新文檔時。EmEditor 內部使用。 |
| `/eh` | 抓取文字塊內容。 |
| `/fc "FindWhat"` | 多檔尋找 (區分大小寫) 。 |
| `/fd` | 顯示 [**多檔尋找** 對話方塊](../../dlg/find_in_files/index)。 |
| `/ff "FindWhat"` | 直接在打開的文檔中尋找一個字串。可以與 /mc 或 /x 聯合使用。 |
| `/fi "FindWhat"` | 多檔尋找 (不區分大小寫) 。 |
| `/fh` | 亮顯被搜尋的字串。 |
| `/fhf` | 用上次搜尋的字串篩選。 |
| `/fn` | 僅顯示檔案名稱當多檔尋找時。 |
| `/fu "FilesToIgnore"` | 忽略下列檔案或資料夾名稱。 |
| `/fr` | 在子資料夾中搜尋當進行多檔尋找時 (與/fc 或 /fi 一起用) 。 |
| `/fw` | 僅搜尋單字 |
| `/hide` | 把 EmEditor 作為一個隱藏的視窗運行當 "快速開始" 選項被啟用時。 |
| `/i` | 從剪貼簿上貼上一個文字字串。 |
| `/ipi` | 重新整理外掛程式清單。從外掛程式安裝程式中使用。 |
| `/iq` | 從剪貼簿上貼上一個文字字串為引用文字。 |
| `/iqr` | 從剪貼簿上貼上一個文字字串為引用文字並換行。 |
| `/ko` | 保持修改的檔案打開當多檔取代時。 |
| `/l LineNumber` | 把游標移到邏輯行的行號處。負數表示從檔案底部開始的行數。 |
| `/layout "Layout"` | 使用指定的版面配置。 |
| `/max limit` | 當符合數達到此數量時停止多檔尋找或取代。 |
| `/mc` | 符合大小寫當 /ff 被用來尋找一個字串時。 |
| `/mf` | 指定一個要運行的巨集檔案。 |
| `/n` | 總是作為一個新檔案開始。 |
| `/ncp` | 隱藏 "指定的檔案不存在。要打開一個新檔案嗎？" 的提示消息當一個指定的檔案無法找到時。<br> 此選項不適用於從工作區恢復檔案。 |
| `/ne` | 指定停用由事件觸發的巨集。 |
| `/ng` | 總是建立一個新的群組視窗。 |
| `/nr` | 不添加檔案路徑到最近檔案清單中。 |
| `/od` | 顯示「打開」對話方塊來選擇要打開的檔案。 |
| `/ol "licenseFilePath"` | 使用[離線授權](../offline_registration/index.md)來註冊 EmEditor。`licenseFilePath` 是授權檔案的路徑。對於桌面安裝，授權信息寫入 `HKEY_CURRENT_USER`；對於可攜式版本，授權信息寫入 `eeCommon.ini`。 |
| `/ola "licenseFilePath"` | 使用[離線授權](../offline_registration/index.md)來註冊 EmEditor。 `licenseFilePath` 是授權檔案的路徑。授權信息寫入 `HKEY_LOCAL_MACHINE`，這需要系統管理員權限。 |
| `/p` | 列印檔案。 |
| `/pos left top right bottom` | 用四個整數指定視窗位置 (左，頂，右，底) 。 |
| `/r` | 唯讀模式。 |
| `/rc "FindWhat"` | 多檔取代 (區分大小寫) 。 |
| `/rd` | 顯示 [**多檔取代** 對話方塊](../../dlg/replace_in_files/index)。 |
| `/rh` | 把 HTML 檔案打開為唯讀。內部使用。 |
| `/ri "FindWhat"` | 多檔取代 (不區分大小寫) 。 |
| `/rr` | 在資料夾中以遞歸方式打開檔案。 |
| `/rw` | 指定要用來取代的字串。 |
| `/sa "DestFile"` | 在轉換編碼後指定一個要儲存為的檔案名稱。 |
| `/sca` | 儲存並關閉所有打開的文檔。 |
| `/scrlf` | 在轉換編碼後用 CR+LF 作為換行方式來儲存檔案。 |
| `/scr` | 在轉換編碼後用僅 CR 作為換行方式來儲存檔案。 |
| `/slf` | 在轉換編碼後用僅 LF 作為換行方式來儲存檔案。 |
| `/sp` | 指定要在其他 EmEditor 視窗中運行一個新的單獨進程。這個選項適用於由於應用程式必須監控進程終止來偵測檔案修改，因此必須從另一個應用程式中啟動一個新的 EmEditor 視窗。如果該選項被指定，一些包括頁面操作在內的功能將被停用，並且會喪失支持。 |
| `/ss+` | 用一個 Unicode 簽名 (BOM) 儲存檔案在在轉換編碼之後。 |
| `/ss-` | 不用一個 Unicode 簽名 (BOM) 儲存檔案在在轉換編碼之後。 |
| `/ti` | 顯示系統匣圖示。 |
| `/uob` | 用匯出欄來顯示多檔尋找的結果。 |
| `/x` | 用規則運算式尋找或多檔尋找。 |
| `/xnr` | 使用數字範圍運算式多檔尋找或尋找。 |
| `/ws` | 還原工作區。 |
| `/wss` | 儲存工作區。 |

## 範例

```
/rr *.htm
```

打開所有 .htm 檔案包括所有子資料夾。

```
/p "filename"
```

匯出檔案名稱。

```
/r "filename"
```

用唯讀模式打開 filename 檔案。

```
/c "Normal" "filename"
```

用預設組態打開 filename 檔案。

```
/l 123 "filename"
```

打開 filename 檔案，跳到第 123 行並顯示。

```
/l -1 "filename"
```

打開 filename 檔案，跳到最後一行並顯示。

```
/ff "what" /mc "filename"
```

打開 filename 檔案，並尋找符合的大小寫。

```
/fh
```

亮顯最後一次搜尋的字串。

```
/ti
```

作為一個系統匣圖示打開。

```
/fi "ABC" "c:\Temp\*.txt"
```

在 c:\\Temp 資料夾中從所有副檔名為 .txt 的檔案中搜尋字串 ABC，並忽略大小寫。

```
/fi "abc" /fr /fw /fn /fu "_*;*.bak" /cp 65536 "c:\test\*.htm;*.txt"
```

在 c:\\test 資料夾中從所有副檔名為 .htm 以及 .txt 的檔案中搜尋字串 abc，並忽略大小寫。另外，該命令的附加條件有搜尋子資料夾，只搜尋字詞，僅顯示檔案名，忽略檔案或資料夾名稱與 "\_\*;\*.bak" 符合，並使用系統預設編碼。

```
/fc "[a-e]" /fr /x /fu "_*;*.bak" /cp 65536 "c:\test\*.htm;*.txt"
```

在 c:\\test 資料夾中從所有副檔名為 .htm 以及 .txt 的檔案中搜尋與規則運算式 \[a-e\] 符合的文字，並且大小寫需符合。另外，該命令的附加條件有搜尋子資料夾，忽略檔案或資料夾名稱與 "\_\*;\*.bak" 符合，並使用系統預設編碼。

```
"c:\test\utf16.txt" /cp 65537 /cps 65001 /ss- /sa "c:\test\utf8.txt" /scrlf
```

不用 Unicode 簽名，把一個 UTF-16LE 檔案，c:\\test\\utf16.txt，轉換為 UTF-8，並儲存為 c:\\test\\utf8.txt。換行方式被轉換為 CR+LF。

## 提示

- 在檔案中搜尋的字串必須跟在 /fc 或 /fi 之後。
- 如果不指定任何選項，被選取的檔案只會被打開。
- 如果 /c 沒有被指定，並且與某個組態相關聯的副檔名相同，那么會用該組態打開檔案。i
- 如果一個資料夾名稱被指定而不是一個檔案名，EmEditor 會用「打開」對話方塊顯示該資料夾。
- 命令列選項區分大小寫。例如 /r 無法被識別如果寫作 /R 的話。
- 當從命令列進行搜尋時，會一直用逸出數列。
- 可以使用連字號（-）代替斜線（/）。例如，可以使用 -sp 代替 /sp。
- 要將 EmEditor 設定為 Git 的預設文字編輯器，請打開 Git Bash 並鍵入：git config --global core.editor "emeditor.exe -sp"。
