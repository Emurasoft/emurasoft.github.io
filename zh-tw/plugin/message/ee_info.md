# EE\_INFO

檢索或設定用於 EmEditor 的信息參數之一的值。您能明確地發送該消息或用
[Editor\_Info](../macro/editor_info)， [Editor\_DocInfo](../macro/editor_docinfo)，或 [Editor\_DocInfoEx](../macro/editor_docinfoex) 內嵌函式。

```
EE_INFO
wParam = (WPARAM)(int)nCmd;
lParam = (LPARAM)lParam;
```

Or

```
EE_INFO
wParam = MAKEWPARAM(nCmd, iDoc+1);
lParam = (LPARAM)lParam;
```

## 參數

_nCmd_

指定要檢索或設置的參數。這個參數可以是下面表格中所列的值之一。

|     |     |     |     |
| --- | --- | --- | --- |
| **nCmd** | **含義** | **lParam** | **返回值** |
| EI\_GET\_ENCODE | 檢索要儲存檔案的編碼方式。 | 不使用。 | (int)nCP<br> 編碼方式。 |
| EI\_SET\_ENCODE | 設置一個儲存檔案的編碼方式。 | (UINT)nCP<br> 指定一個以 CODEPAGE\_ 為開始值的編碼方式。 | 不使用。 |
| EI\_GET\_SIGNATURE | 檢索是否要給 Unicode/UTF-8 檔案簽名。 | 不使用。 | (BOOL)bSignature<br> TRUE，簽名。 |
| EI\_SET\_SIGNATURE | 設置是否要給 Unicode/UTF-8 檔案簽名。 | (BOOL)bSignature<br> TRUE，簽名。 | 不使用。 |
| EI\_GET\_FONT\_CHARSET | 檢索一個要顯示的字元集。 | 不使用。 | (int)nCharset<br> 字元集。 |
| EI\_SET\_FONT\_CHARSET | 設置要一個要顯示的字元集。 | (int)nCharset<br> 指定一個以 CHARSET\_ 為開始值的字元集。 | 不使用。 |
| EI\_GET\_FONT\_CP | 檢索所使用的字型顯示的代碼頁。 | 不使用。 | (UINT)nCP<br> 該代碼頁。 |
| EI\_GET\_INPUT\_CP | 檢索所使用的輸入語言的代碼頁。 | 不使用。 | (UINT)nCP<br> 該代碼頁。 |
| EI\_GET\_SHOW\_TAG | 檢索是否顯示被亮顯的標籤。 | 不使用。 | (BOOL)bShowTag<br> TRUE 表示亮顯標籤。 |
| EI\_SET\_SHOW\_TAG | 設置是否顯示被亮顯的標籤。 | (BOOL)bShowTag<br> TRUE 表示亮顯標籤。 | 不使用。 |
| EI\_GET\_FILE\_NAMEA | 用位元組檢索目前的打開的檔案名。 | (LPSTR)szFileName<br> 指定一個指針指向緩衝區來檢索檔案名。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_FILE\_NAME\_EX | 用 Unicode 檢索當前打開的檔案名。 | (STRING\_BUF\*)pStringBuf<br> 指定一個指針指向檢索檔案名的 [STRING\_BUF](../structure/string_buf) 結構。 | 不使用。 |
| EI\_GET\_FILE\_NAMEW | 檢索目前的打開的檔案名，用 Unicode 表示。 | (LPSTR)szFileName<br> 指定一個指針指向緩衝區來檢索檔案名。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_SET\_FILE\_NAMEW | 重新命名目前打開的檔案名。如果文檔沒有標題，則重新命名文檔標題而不儲存檔案。 | (LPCWSTR)pszName<br> 指定新名稱。 | (HRESULT)hr<br>如果失敗則返回負值。 |
| EI\_IS\_PROPORTIONAL\_FONT | 檢索是否顯示的字型是成比例的。 | 不使用。 | (BOOL)bProportionalFont |
| EI\_GET\_NEXT\_BOOKMARK | 尋找下一個書籤位置。 | (int)yLine<br> 指定一個要搜尋的起始邏輯行位置。-1 會從文檔開始處搜尋。 | (int)yLine<br> 返回被搜尋的邏輯行。-1 會被返回如果沒有被尋找到任何符合的結果的話。 |
| EI\_GET\_HILITE\_FIND | 檢索被搜尋的字串是否被亮顯。 | 不使用。 | (BOOL)bShowFindHilite |
| EI\_SET\_HILITE\_FIND | 設置被搜尋的字串是否被亮顯。 | (BOOL)bShowFindHilite | 不使用。 |
| EI\_GET\_APP\_VERSIONA | 檢索版本名稱為一個 ANSI　字串。 | (LPSTR)szVersionName<br> 指定一個指針指向一個緩衝區來檢索版本字串。緩存區必須是 MAX\_PATH 字元長度包括終止空字元。 | 不使用。 |
| EI\_GET\_APP\_VERSIONW | 檢索版本名稱為一個 Unicode 字串。 | (LPWSTR)szVersionName<br> 指定一個指針指向一個緩衝區來檢索版本字串。緩存區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_READ\_ONLY | 檢索文檔是否為唯讀模式。 | 不使用。 | (BOOL)bReadOnly |
| EI\_IS\_WINDOW\_COMBINED | 檢索視窗是否被合併。 | 不使用。 | (BOOL)bCombined |
| EI\_WINDOW\_COMBINE | 設置視窗是否被合併。 | (BOOL)bCombined<br> 合併視窗如果是 TRUE，或分隔視窗如果是 FALSE。 | 不使用。 |
| EI\_IS\_UNDO\_COMBINED | 檢索一個被插入的字串是否能被立即撤銷。 | 不使用。 | (BOOL)bCombined |
| EI\_GET\_DOC\_COUNT | 檢索在目前的框架視窗中打開文檔的數目 (僅適用於 EmEditor 5.00 或之後的版本)。 | 不使用。 | (int)nCount<br> 返回打開文檔數。 |
| EI\_INDEX\_TO\_DOC | 把一個文檔索引轉換為文檔句柄(僅適用於 EmEditor 5.00 或之後的版本)。 | 指定從零開始的文檔索引。 | (HEEDOC)hDoc<br> 返回文檔的句柄。 |
| EI\_DOC\_TO\_INDEX | 把一個文檔句柄轉換為文檔索引。 | 指定文檔的句柄。 | (int)nIndex<br> 返回從零開始的文檔索引。 |
| EI\_ZORDER\_TO\_DOC | 把一個文檔的疊置順序 (z-order) 轉換為一個文檔句柄。 | 指定從零開始的文檔疊置順序。 | (HEEDOC)hDoc<br> 返回句柄到該文檔中。 |
| EI\_DOC\_TO\_ZORDER | 把一個文檔句柄轉換為一個文檔的疊置順序 (z-order)。 | 為該文檔指定句柄。 | (int)nZOrder<br> 返回從零開始的文檔疊置順序。 |
| EI\_GET\_ACTIVE\_INDEX | 檢索活動文檔的索引。 | 不使用。 | (int)nIndex<br> 返回從零開始的文檔疊置順序。 |
| EI\_SET\_ACTIVE\_INDEX | 激活一個文檔。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
| EI\_GET\_FULL\_TITLEA | 在 ANSI 字串中，檢索文檔的完整標題。 | (LPSTR)szTitle<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_FULL\_TITLEW | 在 Unicode 字串中，檢索文檔的完整標題。 | (LPWSTR)szTitle<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SHORT\_TITLEA | 在 ANSI 字串中，檢索文檔的簡略標題。 | (LPSTR)szTitle<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SHORT\_TITLEW | 在 Unicode 字串中，檢索文檔的簡略標題。 | (LPWSTR)szTitle<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SAVE\_AS\_TITLEA | 檢索文檔的完整標題，除了星號 (\*) 所表示的在 ANSI 字串中的修改。 | (LPSTR)szTitle<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_GET\_SAVE\_AS\_TITLEW | 檢索文檔的完整標題，除了星號 (\*) 所表示的在 Unicode 字串中的修改。 | (LPWSTR)szTitle<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_MOVE\_ORDER | 改變文檔標籤頁順序。 | 指定從零開始的目標標籤頁索引。 | 不使用。 |
| EI\_CLOSE\_DOC | 關閉文檔。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
| EI\_SAVE\_DOC | 儲存文檔。如果文檔未命名，會出現 **另存新檔** 對話方塊。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。當文檔未命名時，在 **另存新檔** 對話方塊中選擇「取消」，也會返回 FALSE。 |
| EI\_GET\_CURRENT\_FOLDER | 檢索目前的運作的資料夾。 | (LPWSTR)szDir<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | 不使用。 |
| EI\_IS\_LARGE\_DOC | 檢索標志來指出文檔是否很大。 | 不使用。 | (BOOL)bLarge<br> 返回 TRUE 如果文檔很大。否則的話，返回 FALSE。 |
| EI\_USE\_INI | 檢索是否用 INI 檔案，而不是注冊表。 | 不使用。 | (BOOL)bIni<br> 返回 TRUE 如果用 INI 檔案，或 FALSE 如果用注冊表。 |
| EI\_GET\_LANGUAGE | 檢索目前的為使用者界面選取的語言。 | (LPWSTR)szFolder<br> 指定要檢索字串的緩衝區。緩衝區必須是 MAX\_PATH 字元長度，包括終止空字元。 | (UINT)nLangID<br> 返回目前的被選取的語言 ID。 |
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
| EI\_GET\_HEADING\_LINES | 檢索標題的行數（非捲動區域）。 | 不使用。 | (int)nHeadingLines |
| EI\_SET\_HEADING\_LINES | 設定標題的行數（非捲動區域）。 | (int)nHeadingLines | 不使用。 |
| EI\_GET\_NARROWING\_TOP | 檢索僅編輯選定區域的首行（y 坐標）。-1 表示未設定僅編輯選定區域。 | 不使用。 | (int)nNarrowingTop |
| EI\_SET\_NARROWING\_TOP | 設定僅編輯選定區域的首行（y 坐標）。-1 表示未設定僅編輯選定區域。 | (int)nNarrowingTop | 不使用。 |
| EI\_GET\_NARROWING\_BOTTOM | 檢索僅編輯選定區域的末行（y 坐標）。-1 表示未設定僅編輯選定區域。 | 不使用。 | (int)nNarrowingBottom |
| EI\_SET\_NARROWING\_BOTTOM | 設定僅編輯選定區域的末行（y 坐標）。-1 表示未設定僅編輯選定區域。 | (int)nNarrowingBottom | 不使用。 |
| EI\_SET\_HILITE\_FILTER | 使用上次使用的尋找信息設定篩選。僅允許使用激活的文檔。 | 不使用。 | 不使用。 |
| EI\_GET\_CSV | 檢索目前的 CSV 模式的索引，如果不是 CSV 模式，則返回 -1。 | 不使用。 | (int)iCSV |
| EI\_GET\_PRINT\_PAGES | 檢索目前指定列印的頁數。僅允許激活的文檔。 | (BOOL)bSelOnly<br>指定是否僅計算選取區域的頁數。 | (int)nPages |
| EI\_GET\_COMBINE\_HISTORY | 檢索能顯示是否要在復原記錄中把下個變更與上一個變更合併為一個的標志。 | 不使用。 | (BOOL)bCombine |
| EI\_GET\_CELL\_MODE | 檢索標志，顯示選擇模式是否是儲存格選擇模式。 | 不使用。 | (BOOL)bCellMode |
| EI\_SET\_CELL\_MODE | 設置標志，顯示選擇模式是否是儲存格選擇模式。 | (BOOL)bCellMode | 不使用。 |
| EI\_GET\_UNTITLED | 檢索顯示文檔是否未命名的標志。 | 不使用。 | (BOOL)bUntitled |
| EI\_GET\_DPI | 檢索目前的監視器的 DPI 值。 | 不使用。 | (long)nDPI |
| EI\_GET\_FILTER\_VISIBLE\_LINES\_ABOVE | 檢索用篩選器符合的行以上的可見行數。 | 不使用。 | (long)nLines |
| EI\_SET\_FILTER\_VISIBLE\_LINES\_ABOVE | 設置用篩選器符合的行以上的可見行數。 | (long)nLines | 不使用。 |
| EI\_GET\_FILTER\_VISIBLE\_LINES\_BELOW | 檢索用篩選器符合的行以下的可見行數。 | 不使用。 | (long)nLines |
| EI\_SET\_FILTER\_VISIBLE\_LINES\_BELOW | 設置用篩選器符合的行以下的可見行數。 | (long)nLines | 不使用。 |
| EI\_GET\_DPI\_OPTIONS | 檢索與螢幕相關的選項。目前只支持 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED。當設置 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED 時，EmEditor 會在 DPI 變更時調整視窗的大小。 | 不使用。 | (long)nFlags |
| EI\_SET\_DPI\_OPTIONS | 設置與螢幕相關的選項。目前只支持 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED。當設置 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED 時，EmEditor 會在 DPI 變更時調整視窗的大小。 | (long)nFlags | 不使用。 |
| EI\_GET\_REGISTERED\_NAME | 檢索注冊名稱，顯示在「關于」對話方塊中。 如果產品未注冊，將檢索空字串。 | (LPWSTR)szName<br>指定要檢索字串的緩沖區。 緩沖區必須為 MAX\_REG\_NAME 字元長度，包括終止 NULL 字元。 | 不使用。 |
| EI\_VALIDATE\_CSV | 驗證CSV文檔和輸出錯誤，并可選擇地調整分隔符位置。 | (int)nFlags<br>你可以指定 VALIDATE\_ADJUST\_COLUMNS，VALIDATE\_QUIET，VALIDATE\_ADJUST\_VISIBLE\_ONLY，VALIDATE\_DETECT\_NL，VALIDATE\_DONT\_CLEAR\_OUTPUT，VALIDATE\_QUIET\_IF\_NO\_ERROR，VALIDATE\_ADJUST\_ENLARGE\_ONLY，VALIDATE\_DETECT\_CSV 和 VALIDATE\_ASYNC 的組合。 | (int)nResults<br>返回值是 CSV\_ADJUSTED，CSV\_NL\_EMBEDDED，CSV\_ABORT，CSV\_INVALID\_QUOTES，CSV\_INCONSISTENT\_COLUMNS，CSV\_NOT\_CSV，CSV\_ASYNC\_SUCCESS 和 CSV\_ASYNC\_RUNNING 的組合。返回值為 0 表示沒有錯誤。 |
| EI\_GET\_CLIENT\_RECT\_NO\_BARS | 檢索編輯器視圖的坐標，不包括捲軸和迷你地圖占用的區域。 | (RECT\*)pRect | 如果成功，返回 TRUE；如果失敗，返回 FALSE。 |
| EI\_REFRESH\_COMMON\_SETTINGS | 加載常用設置並重新整理 EmEditor 視窗。 | 不使用。 | 不使用。 |
| EI\_GET\_NEWLINE\_CODE | 檢索文檔中使用的新行字元碼。 | 不使用。 | 返回 FLAG\_CR\_AND\_LF，FLAG\_CR\_ONLY，FLAG\_LF\_ONLY，或 FLAG\_NEWLINE\_MIXED。 |
| EI\_GET\_MEMORY\_SIZE | 檢索文檔中使用的記憶體大小。可以在 **自訂** 對話方塊的 [**進階** 頁面](../../dlg/customize/advanced/index) 上的 **記憶體大小** 文字方塊中指定預設值。 | 不使用。 | 返回記憶體大小。 |
| EI\_SET\_MEMORY\_SIZE | 設置文檔中使用的記憶體大小。可以在 **自訂** 對話方塊的 [**進階** 頁面](../../dlg/customize/advanced/index) 上的 **記憶體大小** 文字方塊中指定預設值。 | (long)nBits<br>指定所需的記憶體大小。 | 返回新的記憶體大小。如果文檔已經使用大於指定大小的記憶體大小，則此值可能會大於指定的大小。 |
| EI\_GET\_BOOKMARK\_COUNT | 檢索文檔中的書籤數。 | 不使用。 | 返回文檔中的書籤數。 |
| EI\_SYNC\_NOW | 觸發 EmEditor 立即同步。 | (UINT)nFlags<br>你可以指定 SYNC\_FLAG\_SEND，SYNC\_FLAG\_RECEIVE，SYNC\_FLAG\_FORCE，和 SYNC\_FLAG\_REFRESH\_UI 的組合。 | 不使用。 |
| EI\_GET\_CHAR\_TYPE | 檢索字元類型。 | (LPCWSTR)pch | 返回字元類型。它可以是下列類型之一：<br>CHAR\_NULL，CHAR\_SPACE，CHAR\_MARK，CHAR\_ALPHANUMERIC，CHAR\_KANA ，CHAR\_KANA\_MARK ，CHAR\_DB\_SPACE，CHAR\_DB\_MARK，CHAR\_DB\_ALPHANUMERIC，CHAR\_DB\_HIRA，CHAR\_DB\_KATA，CHAR\_DB\_KANJI，CHAR\_DB\_KANA\_MARK，CHAR\_SECOND\_DB，CHAR\_HANGUL，CHAR\_DB\_HANGUL。 |
| EI\_FILE\_POS\_TO\_LOGICAL | 將檔案位置轉換為邏輯位置。 | (FILE\_POS\_INFO\*)pFilePosInfo | 不使用。 |
| EI\_LOGICAL\_TO\_FILE\_POS | 將邏輯位置轉換為檔案位置。 | (FILE\_POS\_INFO\*)pFilePosInfo | 不使用。 |
| EI\_CELL\_TO\_LOGICAL | 將儲存格位置轉換為邏輯位置。 | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | 不使用。 |
| EI\_LOGICAL\_TO\_CELL | 將邏輯位置轉換為儲存格位置。 | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | 不使用。 |
| EI\_IS\_VERY\_DARK | 檢查系統是否支持夜間模式，如果支持，則檢查使用者是否選擇了很暗模式。 | 不使用。 | 如果使用者選擇了很暗模式，則返回 TRUE；否則，返回FALSE；如果系統不支援夜間模式，則返回 NOT\_SUPPORTED。 |
| EI\_WM\_INITDIALOG | 在對話方塊程序中的 WM\_INITDIALOG 消息內部呼叫，以支持很暗模式。 | (HWND)hWnd | 不使用。 |
| EI\_WM\_CTLCOLOR | 在對話方塊程序中的 WM\_CTLCOLORDLG，WM\_CTLCOLORSTATIC，WM\_CTLCOLOREDIT，WM\_CTLCOLORBTN，以及 WM\_CTLCOLORLISTBOX 消息內部呼叫，以支持很暗的模式。 | (WPARAM)wParam<br>您可以轉發傳遞 WM\_CTLCOLORxxx 消息。 | 如果選擇了很暗模式，則返回畫筆。您必須將此值傳遞給對話方塊程序的返回值。 |
| EI\_WM\_THEMECHANGED | 在對話方塊程序中的 WM\_THEMECHANGED 消息內部呼叫，以支持很暗的模式。 | (HWND)hWnd | 不使用。 |
| EI\_INIT\_LISTVIEW | 初始化一個清單視圖控件以支持很暗模式。 | (HWND)hWnd | 不使用。 |
| EI\_GET\_VIEW\_FONT | 檢索目前的選擇的編輯器字型的控點。 | 不使用。 | (HFONT)hFont |
| EI\_GET\_HIDE\_QUOTES | 檢索一個標志，該標志指示在 CSV 儲存格選擇模式下是否啟用了「隱藏引號」顯示畫面。 | 不使用。 | (BOOL)bHideQuotes |
| EI\_SET\_HIDE\_QUOTES | 設定一個標志，該標志指示在 CSV儲存格選擇模式下是否啟用了「隱藏引號」顯示畫面。 | (BOOL)bHideQuotes | 不使用。 |
| EI\_ENABLE\_WM\_CHAR | 內部使用。 | 不使用。 | 內部使用。 |
| EI\_GET\_SYNC | 檢索同步資料夾的路徑。 | (LPWSTR)szDir<br>指定用於檢索字串的緩沖區。緩沖區必須是 MAX\_PATH 字元長，包括終止的 NULL 字元。 | 返回包括 SYNC\_SETTINGS\_SEND 和 SYNC\_SETTINGS\_RECEIVE 的值的組合。 |
| EI\_GET\_SPLIT | 檢索分割狀態。 | 不使用。 | 返回以下值之一：SPLIT\_NONE，SPLIT\_HORZ，SPLIT\_VERT，SPLIT\_BOTH，SPLIT\_2\_HORZ，或 SPLIT\_2\_VERT。 |
| EI\_GET\_SUM | 檢索所選內容中包含的數字的總和以及次數。 | (SUM\_INFO\*)pSumInfo | 如果成功返回 TRUE，如果失敗則返回 FALSE。 |
| EI\_GET\_CONFIG | 檢索選取的組態名稱。 | 指定指向緩沖區的指針以檢索組態名稱。緩沖區的長度必須為 MAX\_CONFIG\_NAME 指定的字元，包括終止 NULL 字元。 | 不使用。 |
| EI\_SET\_CONFIG | 對指定組態的變更。 | 指定一個組態名稱。 | (BOOL)bSuccess |
| EI\_SAVE\_FILE | 儲存一個文件。 | 指定完整的檔案路徑名稱。 | (BOOL)bSuccess |
| EI\_INDEX\_TO\_DOC\_REAL | 將文件索引轉換為文件控點。與 EI\_INDEX\_TO\_DOC 不同，此命令計算在分割視窗中唯一的單個文件。 | 指定從零開始的文件索引。 | (HEEDOC)hDoc<br>返回文件的控點。 |
| EI\_DOC\_TO\_INDEX\_REAL | 將文件索引轉換為文件控點。與 EI\_INDEX\_TO\_DOC 不同，此命令計算在分割視窗中唯一的單個文件。 | 指定文件的控點。 | (int)nIndex<br>返回從零開始的文件索引。 |
| EI\_GET\_TITLE | 檢索目前的文檔的標題。 | (STRING\_BUF\*)pStringBuf<br> 指定指針指向一個檢索標題的 [STRING\_BUF](../structure/string_buf) 結構。 | 不使用。 |
| EI\_SET\_TITLE | 設定目前的文檔的標題。標題可能包含由換行符 (\\n) 分隔的長標題和短標題。 | (LPCWSTR)pszTitle<br> 指定一個新標題。 | (HRESULT)hr<br>如果失敗，則返回負值。 |
| EI\_SET\_WEB | 設定網頁瀏覽器的旗標。 | (UINT)nFlags<br> 指定一個新旗標。 | 不使用。 |
| EI\_OPEN\_WEB | 打開指定 URL 的網站。 | (LPCWSTR)pszURL<br> 指定一個 URL。 | (HRESULT)hWnd<br> 返回網頁檢視的視窗控點。 |
| EI\_GET\_MARKDOWN\_PREVIEW | 檢索是否設定了 Markdown 設計檢視。 | 不使用。 | (BOOL)bMarkdownPreview<br> 如果為 TRUE，則是 Markdown 設計檢視 |
| EI\_SET\_MARKDOWN\_PREVIEW | 切換 Markdown 設計檢視 | (BOOL)bMarkdownPreview<br> 如果為 TRUE，則是 Markdown 設計檢視 | 不使用。 |
| EI\_IS\_CHATAI\_INSTALLED | 檢索是否安裝了 ChatAI 外掛程式。 | 不使用。 | (BOOL)bInstalled<br> 如果為 TRUE，則是 Markdown 設計檢視 |
| EI_RESET_BOOKMARK | 重設文檔中指定的書籤或所有打開的文檔中的所有書籤。 | (INT\_PTR)y<br>指定要重設書籤的行號，如果為 -1，則重設所有打開的文檔中的所有書籤。 | 不使用。 |
| EI_BRING_CUSTOM_BAR_TOP | 將指定的自訂欄置於頂部。 | (HWND)hwndClient<br>指定客戶端視窗 | (int)iCustomBar<br>指定自訂欄的位置，如果未找到則為 -1。 |

_iDoc_

指定目標文件的索引。指定目標文件的索引。應當指定一個從 1 開始的索引在 wParam 參數的高字處。如果 wParam 參數的高字處指定了 0，那么目前使用中的文件就會成為目標文件。根據不同的 nCmd，這個參數也有可能不被使用。如果是這個情況，那么 wParam 的高字一定是 0。

_lParam_

取決于指定的參數。

## 返回值

取決于指定的參數。

## 支持版本

支持 EmEditor 3.00 或之後的版本。 然而，iDoc 參數僅在 EmEditor 5.00 或之後的版本上支持。
