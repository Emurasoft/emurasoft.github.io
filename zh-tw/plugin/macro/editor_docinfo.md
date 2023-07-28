# Editor\_DocInfo

檢索或設置用於 EmEditor 的信息參數之一的值。您能直接用該內嵌函式或明確地發送
[EE\_INFO](../message/ee_info) 消息。

Editor\_DocInfo( HWND hwnd, int iDoc, int nCmd, LPARAM lParam );

## 參數

_nCmd_

指定要檢索或設置的參數。這個參數可以是下面表格中所列的值之一。

|     |     |     |     |
| --- | --- | --- | --- |
| **nCmd** | **含義** | **lParam** | **返回值** |
| EI\_GET\_ENCODE | 檢索要儲存檔案的編碼方式。 | 不使用。 | 編碼方式。 |
| EI\_SET\_ENCODE | 設置一個儲存檔案的編碼方式。 | (UINT)nCP<br> 指定一個以 CODEPAGE\_ 為開始值得編碼方式。 | 不使用。 |
| EI\_GET\_SIGNATURE | 檢索是否要給 Unicode/UTF-8 檔案簽名。 | 不使用。 | (BOOL)bSignature<br> TRUE to sign. |
| EI\_SET\_SIGNATURE | 設置是否要給 Unicode/UTF-8 檔案簽名。 | (BOOL)bSignature<br> TRUE to sign. | 不使用。 |
| EI\_GET\_FONT\_CHARSET | 檢索一個要顯示的字元集。 | 不使用。 | (int)nCharset<br> 字元集。 |
| EI\_SET\_FONT\_CHARSET | 設置要一個要顯示的字元集。 | (int)nCharset<br> 指定一個以 CHARSET\_ 為開始值的字元集。 | 不使用。 |
| EI\_GET\_FONT\_CP | 檢索所使用的字型顯示的代碼頁。 | 不使用。 | (UINT)nCP<br> 該代碼頁。 |
| EI\_GET\_INPUT\_CP | 檢索所使用的輸入語言代碼頁。 | 不使用。 | (UINT)nCP<br> 該代碼頁。 |
| EI\_GET\_SHOW\_TAG | 檢索是否顯示被亮顯的標籤。 | 不使用。 | (BOOL)bShowTag<br> TRUE 表示亮顯標籤。 |
| EI\_SET\_SHOW\_TAG | 設置是否顯示被亮顯的標籤。 | (BOOL)bShowTag<br> TRUE 表示亮顯標籤。 | 不使用。 |
| EI\_GET\_FILE\_NAMEA | 檢索目前的打開的檔案名，用位元表示。 | (LPSTR)szFileName<br> 指定一個指標至緩沖區來檢索檔案名。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_FILE\_NAMEW | 檢索目前的打開的檔案名，用 Unicode 表示。 | (LPSTR)szFileName<br> 指定一個指標至緩沖區來檢索檔案名。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_IS\_PROPORTIONAL\_FONT | 檢索是否顯示的字型是成比例的。 | 不使用。 | (BOOL)bProportionalFont |
| EI\_GET\_NEXT\_BOOKMARK | 尋找下一個書籤位置。 | (int)yLine<br> 指定一個要搜尋的起始邏輯行位置。-1 會從文檔開始處搜尋。S | (int)yLine<br> 返回被搜尋的邏輯行。-1 會被返回如果沒有被尋找到任何符合的結果的話。 |
| EI\_GET\_HILITE\_FIND | 檢索被搜尋的字串是否被亮顯。 | 不使用。 | (BOOL)bShowFindHilite |
| EI\_SET\_HILITE\_FIND | 設置被搜尋的字串是否被亮顯。 | (BOOL)bShowFindHilite | 不使用。 |
| EI\_GET\_APP\_VERSIONA | 把版本名稱作為一個 ANSI 字串進行檢索。 | (LPSTR)szVersionName<br> 指定一個指標至一個緩沖區來檢索版本字串。緩存區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_APP\_VERSIONW | 把版本名稱作為一個 Unicode 字串進行檢索。 | (LPWSTR)szVersionName<br> 指定一個指標至一個緩沖區來檢索版本字串。緩存區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_READ\_ONLY | 檢索文檔是否為唯讀模式。 | 不使用。 | (BOOL)bReadOnly |
| EI\_IS\_WINDOW\_COMBINED | 檢索視窗是否被合併。 | 不使用。 | (BOOL)bCombined |
| EI\_WINDOW\_COMBINE | 設置視窗是否被合併。 | (BOOL)bCombined<br> 合併視窗如果是 TRUE，或分隔視窗如果是 FALSE。 | 不使用。 |
| EI\_IS\_UNDO\_COMBINED | 檢索一個被插入的字串是否能被立即撤銷。 | 不使用。 | (BOOL)bCombined |
| EI\_GET\_DOC\_COUNT | 檢索在目前的框架視窗中打開文檔的數目 (僅適用於 EmEditor 5.00 或之後的版本)。 | 不使用。 | (int)nCount<br> 返回打開文檔的數目。 |
| EI\_INDEX\_TO\_DOC | 把一個文檔索引轉換為文句柄(僅適用於 EmEditor 5.00 或之後的版本)。 | 指定從零開始的文檔索引。 | (HEEDOC)hDoc<br> 返回文檔的句柄。 |
| EI\_DOC\_TO\_INDEX | 把一個文檔句柄轉換為文索引。 | 指定文檔的句柄。 | (int)nIndex<br> 返回從零開始的文檔索引。 |
| EI\_ZORDER\_TO\_DOC | 把一個文檔的疊置順序 (z-order) 轉換為一個文檔句柄。 | 指定從零開始的文檔疊置順序。 | (HEEDOC)hDoc<br> 返回句柄到該文檔中。 |
| EI\_DOC\_TO\_ZORDER | 把一個文檔句柄轉換為一個一個文檔的疊置順序 (z-order)。 | 為該文檔指定句柄。 | (int)nZOrder<br> 返回從零開始的文檔疊置順序。 |
| EI\_GET\_ACTIVE\_INDEX | 檢索活動文檔的索引。 | 不使用。 | (int)nIndex<br> 返回從零開始的文檔疊置順序。 |
| EI\_SET\_ACTIVE\_INDEX | 激活一個文檔。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
| EI\_GET\_FULL\_TITLEA | 在 ANSI 字串中，檢索文檔的完整標題。 | (LPSTR)szTitle<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_FULL\_TITLEW | 在 Unicode 字串中，檢索文檔的完整標題。 | (LPWSTR)szTitle<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SHORT\_TITLEA | 在 ANSI 字串中，檢索文檔的簡略標題。 | (LPSTR)szTitle<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SHORT\_TITLEW | 在 Unicode 字串中，檢索文檔的簡略標題。 | (LPWSTR)szTitle<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SAVE\_AS\_TITLEA | 檢索文檔的完整標題，除了星號 (\*) 所表示的在 ANSI 字串中的修改。 | (LPSTR)szTitle<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SAVE\_AS\_TITLEW | 檢索文檔的完整標題，除了星號 (\*) 所表示的在 Unicode 字串中的修改。 | (LPWSTR)szTitle<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_MOVE\_ORDER | 改變文檔標籤頁順序。 | 指定從零開始的目標標籤頁索引。 | 不使用。 |
| EI\_CLOSE\_DOC | 關閉文檔。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
| EI\_SAVE\_DOC | 儲存文檔。如果文檔未命名，會出現 **另存新檔** 對話方塊。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。當文檔未命名時，在 **另存新檔** 對話方塊中選擇「取消」，也會返回 FALSE。 |
| EI\_GET\_CURRENT\_FOLDER | 檢索目前的運作的資料夾。 | (LPWSTR)szDir<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_IS\_LARGE\_DOC | 檢索標志來指出文檔是否很大。 | 不使用。 | (BOOL)bLarge<br> 返回 TRUE 如果文檔很大。否則的話，返回 FALSE。 |
| EI\_USE\_INI | 檢索是否用 INI 檔案，而不是注冊表。 | 不使用。 | (BOOL)bIni<br> 返回 TRUE 如果用 INI 檔案，或 FALSE 如果用注冊表。 |
| EI\_GET\_LANGUAGE | 檢索目前的為使用者界面選取的語言。 | (LPWSTR)szFolder<br> 指定要檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長度，包括終止空字元。 | (UINT)nLangID<br> 返回目前的被選取的語言 ID。 |
| EI\_COMBINE\_HISTORY | 指定是否要合併上一變更與下一變更，讓它們一起作為一個復原記錄。 | (BOOL)bCombine<br> 合併的話，返回 TRUE。 | 不使用。 |
| EI\_GET\_BAR\_TEXT\_COLOR | 檢索自訂顯示條的文字顏色。 | 不使用。 | (COLORREF)clrText<br> 返回文字顏色的 RGB 值。 |
| EI\_GET\_BAR\_BACK\_COLOR | 檢索自訂顯示條的背景顏色。Retrieves the background color of custom bars. | 不使用。 | (COLORREF)clrBack<br> 返回背景顏色的 RGB 值。 |
| EI\_GET\_RETURN\_TYPE | 檢索目前的行的換行方式。如果目前的行是文檔的最后一行，并且沒有換行，那就檢索前一行的換行方式。 | (UINT\_PTR)yLogicalLine<br> 指定邏輯行的索引。 | (int)nReturnType<br> 返回 RETURN\_METHOD\_BOTH，RETURN\_METHOD\_CR\_ONLY，或 RETURN\_METHOD\_LF\_ONLY。 |
| EI\_GET\_ACTIVE\_DOC | 檢索活動文檔的句柄。 | 不使用。 | (HEEDOC)hDoc<br> 返回該文檔的句柄。 |
| EI\_SET\_ACTIVE\_DOC | 激活一個文檔。 | (HEEDOC)hDoc<br>指定要被激活文檔的句柄。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
| EI\_GET\_SYNC\_SESSION | 檢索文檔的時段 ID，如果文檔在比較或同步捲動模式中。 | 不使用。 | (int)nSessionID<br> 返回時段 ID，如果文檔在比較或同步捲動模式中。返回 0，如果文檔是標準模式。 |
| EI\_GET\_LOC\_DLL\_INSTANCE | 檢索本地化資源 DLL 實例的句柄。 | 不使用。 | (HINSTANCE)hinstLoc<br> 返回本地化資源 DLL 實例的句柄。 |
| EI\_GET\_RES\_DLL\_INSTANCE | 檢索資源 DLL 實例的句柄。 | 不使用。 | (HINSTANCE)hinstRes<br> 返回資源 DLL 實例的句柄。 |
| EI\_GET\_CMD\_LIST\_SIZE | 檢索指定多項功能表命令中可用的項目數。 | 多項功能表命令 ID 的第一個項目。T | (int)nCount<br>返回可用的項目數。 |
| EI\_GET\_DISCARD\_UNDO | 檢索標志，為了指出是否要 EmEditor 丟棄復原信息來提高取代，插入或刪除的速度。 | 不使用。 | (BOOL)bDiscardUndo<br>Returns the flag. |
| EI\_SET\_DISCARD\_UNDO | 設置標志，為了指出是否要 EmEditor 丟棄復原信息來來提高取代，插入或刪除的速度。 | (BOOL)bDiscardUndo<br>The flag. | 不使用。 |

_iDoc_

指定從零開始的目標文檔的索引。如果指定值為 -1，目前的活動文檔會被設為目標文檔。

_lParam_

取決于指定的參數。

## 返回值

取決于指定的參數。

## 支持版本

支持 EmEditor 5.00 或之後的版本。
