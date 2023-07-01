# 內嵌函式

|     |     |
| --- | --- |
| [Editor\_ActivateTemp](editor_activatetemp) | 激活臨時文字。 |
| [Editor\_AddRef](editor_addref) | 遞增外掛程式的引用號。 |
| [Editor\_AutoFill](editor_autofill) | 對 CSV 文檔執行自動填滿或快速填入操作。 |
| [Editor\_BatchFindInFiles](editor_batchfindinfiles) | 從指定路徑中的多個檔案中搜索多個字串。 |
| [Editor\_BatchFindReplace](editor_batchfindreplace) | 搜索或取代多個字串。 |
| [Editor\_BatchReplaceInFiles](editor_batchreplaceinfiles) | 在指定位置取代多個檔案中的多個字串。 |
| [Editor\_CloseTemp](editor_closetemp) | 關閉臨時文字。 |
| [Editor\_Compare](editor_compare) | 比較兩個檔案。 |
| [Editor\_Convert](editor_convert) | 轉換字元。 |
| [Editor\_ConvertCsv](editor_convertcsv) | 轉換目前的文檔的 CSV 格式。 |
| [Editor\_CustomBarOpen](editor_custombaropen) | 打開自訂顯示條。 |
| [Editor\_CustomBarClose](editor_custombarclose) | 關閉自訂顯示條。 |
| [Editor\_DevToView](editor_devtoview) | 轉換指定位置的設備 (客戶端) 坐標來顯示坐標。 |
| [Editor\_DocGetConfigA](editor_docgetconfiga) | 用一個 ANSI 字串檢索選取的組態名稱。 |
| [Editor\_DocGetConfigW](editor_docgetconfigw) | 為指定的文檔檢索選取的組態名稱并把它作為一個 Unicode 字串。 |
| [Editor\_DocGetLines](editor_docgetlines) | 檢索指定文檔的行數。 |
| [Editor\_DocGetModified](editor_docgetmodified) | 檢索指定文檔的文字的修改狀態。 |
| [Editor\_DocInfo](editor_docinfo) | 檢索或設置用於 EmEditor 的信息參數之一的值。 |
| [Editor\_DocInfoEx](editor_docinfoex) | 檢索或設置用於 EmEditor 的信息參數之一的值。 |
| [Editor\_DocSaveFileA](editor_docsavefilea) | 儲存指定文檔中的文字到另一個指定的檔案中 (ANSI)。 |
| [Editor\_DocSaveFileW](editor_docsavefilew) | 儲存指定文檔中的文字到另一個指定的檔案中 (Unicode)。 |
| [Editor\_DocSetConfigA](editor_docsetconfiga) | 把指定文檔變更為一個用 ANSI 字串指定的組態。 |
| [Editor\_DocSetConfigW](editor_docsetconfigw) | 把指定文檔變更為一個用 Unicode 字串指定的組態。 |
| [Editor\_DoIdle](editor_doidle) | 重新整理工具列，視窗標題，標籤頁及其他。 |
| [Editor\_EditColumn](editor_editcolumn) | 移動，復制，刪除，或合併目前的 CSV 文檔中的指定欄。 |
| [Editor\_EditTemp](editor_edittemp) | 把臨時文字作為一個新文檔打開。 |
| [Editor\_EnumConfig](editor_enumconfig) | 列舉可用的組態。 |
| [Editor\_EnumHighlight](editor_enumhighlight) | 列舉亮顯的字串。 |
| [Editor\_EmptyUndoBuffer](editor_emptyundobuffer) | 為復原和重做命令清空緩衝區。 |
| [Editor\_ExecCommand](editor_execcommand) | 執行一個指定的命令。 |
| [Editor\_ExecPlugin](editor_execplugin) | 執行一個指定的外掛程式。 |
| [Editor\_ExtractFrequent](editor_extractfrequent) | 將常用字串抽出到新文檔中。 |
| [Editor\_Filter](editor_filter) | 用指定的字串以及設定來篩選文檔。 |
| [Editor\_FindA](editor_finda) | 搜尋一個 ANSI 字串。 |
| [Editor\_FindInFiles](editor_findinfiles) | 在指定路徑的多個檔案中搜尋一個字串。 |
| [Editor\_FindInFilesA](editor_findinfilesa) | 在指定路徑的多個檔案中搜尋一個 ANSI 字串。 |
| [Editor\_FindInFilesW](editor_findinfilesw) | 在指定路徑的多個檔案中搜尋一個 Unicode 字串。 |
| [Editor\_FindRegex](editor_findregex) | 用規則運算式搜尋一個字串。 |
| [Editor\_FindReplace](editor_findreplace) | 搜尋或取代一個字串。 |
| [Editor\_FindW](editor_findw) | 搜尋一個 Unicode 字串。 |
| [Editor\_Free](editor_free) | 釋放一個指定的外掛程式。 |
| [Editor\_GetAccelArray](editor_getaccelarray) | 檢索快速鍵的數組。 |
| [Editor\_GetActiveString](editor_getactivestring) | 檢索主動字串。 |
| [Editor\_GetAnchorPos](editor_getanchorpos) | 檢索選區的原點。 |
| [Editor\_GetAttr](editor_getattr) | 在剪貼簿記錄中的指定位置處刪除文字。 |
| [Editor\_GetCaretPos](editor_getcaretpos) | 檢索目前的游標位置。 |
| [Editor\_GetCell](editor_getcell) | 在指定的單元格內檢索 Unicode 文字。 |
| [Editor\_GetClip](editor_getclip) | 在剪貼簿記錄中的指定位置處檢索文字。 |
| [Editor\_GetClipPos](editor_getclippos) | 檢索剪貼簿記錄中的目前的位置。 |
| [Editor\_GetCmdID](editor_getcmdid) | 獲得外掛程式命令 ID。 |
| [Editor\_GetColor](editor_getcolor) | 檢索指定部分的文字、背景顏色以及樣式。 |
| [Editor\_GetColumn](editor_getcolumn) | 在 CSV 模式中設置一欄文字。 |
| [Editor\_GetConfigA](editor_getconfiga) | 檢索所選取的組態名稱為 ANSI 字串。 |
| [Editor\_GetConfigW](editor_getconfigw) | 檢索所選取的組態名稱為 Unicode 字串。 |
| [Editor\_GetDroppedFile](editor_getdroppedfile) | 檢索最近拖放的檔案。 |
| [Editor\_GetFilter](editor_getfilter) | 檢索當前文檔的篩選字符串及設定。 |
| [Editor\_GetLineA](editor_getlinea) | 在指定行檢索 ANSI 文字。 |
| [Editor\_GetLines](editor_getlines) | 檢索目前的文檔的行數。 |
| [Editor\_GetLineW](editor_getlinew) | 檢索指定行的 Unicode 文字。 |
| [Editor\_GetMargin](editor_getmargin) | 檢索邊距大小。 |
| [Editor\_GetModified](editor_getmodified) | 檢索文字的修改狀態。 |
| [Editor\_GetMultiSel](editor_getmultisel) | 當多個選區都可用時，檢索一個指定選區的信息。 |
| [Editor\_GetOutlineLevel](editor_getoutlinelevel) | 檢索指定邏輯行的大綱級別。 |
| [Editor\_GetOutputString](editor_getoutputstring) | 檢索輸出列中的文字。 |
| [Editor\_GetPageSize](editor_getpagesize) | 檢索頁面大小。 |
| [Editor\_GetRef](editor_getref) | 檢索一個指定外掛程式的引用號。 |
| [Editor\_GetRedraw](editor_getredraw) | 檢索在 EmEditor 中允許或禁止重繪變更的標志。 |
| [Editor\_GetScrollPos](editor_getscrollpos) | 檢索捲軸的目前的游標位置。 |
| [Editor\_GetSelEnd](editor_getselend) | 檢索選區的結尾字元位置。 |
| [Editor\_GetSelStart](editor_getselstart) | 檢索選區的開始字元位置。 |
| [Editor\_GetSelTextA](editor_getseltexta) | 檢索被選取的 ANSI 文字。 |
| [Editor\_GetSelTextW](editor_getseltextw) | 檢索被選取的 Unicode 文字。 |
| [Editor\_GetSelType](editor_getseltype) | 獲得選區狀態的類型。 |
| [Editor\_GetSelTypeEx](editor_getseltypeex) | 獲得選區狀態的類型。 |
| [Editor\_GetStatusA](editor_getstatusa) | 檢索顯示在狀態列上的 ANSI 文字。 |
| [Editor\_GetStatusW](editor_getstatusw) | 檢索顯示在狀態列上的 Unicode 文字。 |
| [Editor\_GetUnicodeName](editor_getunicodename) | 檢索指定字元或字串的 Unicode 名。 |
| [Editor\_GetVersion](editor_getversion) | 返回版本號。 |
| [Editor\_GetWord](editor_getword) | 檢索游標位置處的一個單字。 |
| [Editor\_Help](editor_help) | 顯示說明中的指定頁面。 |
| [Editor\_Info](editor_info) | 檢索或設置用於 EmEditor 的信息參數之一的值。 |
| [Editor\_InsertA](editor_inserta) | 把一個 ANSI 字串插入到目前的游標位置處。 |
| [Editor\_InsertClip](editor_insertclip) | 在剪貼簿記錄上的指定位置處插入文字。 |
| [Editor\_InsertFileA](editor_insertfilea) | 在游標處插入指定檔案內容　(ANSI)。 |
| [Editor\_InsertFileW](editor_insertfilew) | 在游標處插入指定檔案內容 (Unicode)。 |
| [Editor\_InsertStringA](editor_insertstringa) | 把一個 ANSI 字串插入到目前的游標位置處。取決于目前的屬性，這可能會覆寫已存在的字串。 |
| [Editor\_InsertStringW](editor_insertstringw) | 把一個 Unicode 字串插入到目前的游標位置處。取決于目前的屬性，這可能會覆寫已存在的字串。 |
| [Editor\_InsertW](editor_insertw) | 把一個 Unicode 字串插入到目前的游標位置處。 |
| [Editor\_IsCharHalfOrFull](editor_ischarhalforfull) | 決定一個指定的字元是全形還是半形。它也可以計算指定字串的總寬度。 |
| [Editor\_Join](editor_join) | 按指定索引鍵資料欄,用一個與 JOIN 操作類似的方法合併兩個 CSV 文檔,并創建一個新文檔。 |
| [Editor\_KeyboardProp](editor_keyboardprop) | 顯示指定命令 ID 和組態的鍵盤屬性。 |
| [Editor\_LineFromChar](editor_linefromchar) | 檢索包含指定字元索引 (序列位置) 的行的索引。 |
| [Editor\_LineIndex](editor_lineindex) | 檢索在 EmEditor 中一個指定行的第一個字元的字元索引。 |
| [Editor\_LoadConfigA](editor_loadconfiga) | 重新載入由一個 ANSI 字串指定名稱的組態。 |
| [Editor\_LoadConfigW](editor_loadconfigw) | 重新載入由一個 Unicode 字串指定名稱的組態。 |
| [Editor\_LoadFileA](editor_loadfilea) | 把一個指定檔案載入到 EmEditor 中　(ANSI)。 |
| [Editor\_LoadFileW](editor_loadfilew) | 把一個指定檔案載入到 EmEditor 中　(Unicode)。 |
| [Editor\_LogicalToSerial](editor_logicaltoserial) | 把邏輯坐標轉換為序列位置。 |
| [Editor\_LogicalToView](editor_logicaltoview) | 把邏輯坐標轉換為顯示坐標。 |
| [Editor\_ManageDuplicates](editor_manageduplicates) | 刪除或把重複行設為書籤。 |
| [Editor\_MatchRegex](editor_matchregex) | 決定一個字串是否與一個指定的規則運算式相符合。 |
| [Editor\_Numbering](editor_numbering) | 在游標位置或垂直選擇處，插入編號。 |
| [Editor\_OutputDir](editor_outputdir) | 為輸出列設置目前的目錄。 |
| [Editor\_OutputString](editor_outputstring) | 追加一個字串到輸出列中。 |
| [Editor\_OverwriteA](editor_overwritea) | 通過在目前的游標位置處覆寫已存在的字串插入一個 ANSI 字串。 |
| [Editor\_OverwriteW](editor_overwritew) | 通過在目前的游標位置處覆寫已存在的字串插入一個 Unicode 字串。 |
| [Editor\_PivotTable](editor_pivottable) | 在 CSV 文檔中建立樞紐分析表。 |
| [Editor\_QueryStatus](editor_querystatus) | 查詢命令的狀態，無論命令是否被啟用，也不管命令是否處于被選中的狀態。 |
| [Editor\_QueryString](editor_querystring) | 查詢與指定的命令相關聯的字串。 |
| [Editor\_QueryStringEx](editor_querystringex) | 查詢與指定的命令相關聯的字串。此內嵌函式支持超過 MAX\_PATH 的長檔案路徑。 |
| [Editor\_RearrangeColumns](editor_rearrangecolumns) | 重排 CSV 欄。 |
| [Editor\_Redraw](editor_redraw) | 在 EmEditor 中允許或禁止重繪變更。 |
| [Editor\_RegQueryValue](editor_regqueryvalue) | 根據 EmEditor 的設定，從注冊表或一個 INI 檔案中查詢一個值。 |
| [Editor\_RegSetValue](editor_regsetvalue) | 根據 EmEditor 的設定，設一個值到注冊表或一個 INI 檔案中。 |
| [Editor\_Release](editor_release) | 遞減外掛程式的引用號。 |
| [Editor\_RemoveClip](editor_removeclip) | 在剪貼簿記錄上的指定位置處刪除文字。 |
| [Editor\_ReplaceA](editor_replacea) | 取代一個 ANSI 字串。 |
| [Editor\_ReplaceW](editor_replacew) | 取代一個 Unicode 字串。 |
| [Editor\_ReplaceInFiles](editor_replaceinfiles) | 在指定位置的多個檔案中取代一個字串。 |
| [Editor\_ReplaceInFilesA](editor_replaceinfilesa) | 在指定位置的多個檔案中搜尋一個 ANSI 字串。 |
| [Editor\_ReplaceInFilesW](editor_replaceinfilesw) | 在指定位置的多個檔案中取代一個 Unicode 字串。 |
| [Editor\_RotateClip](editor_rotateclip) | 在剪貼簿記錄上旋轉目前的位置。 |
| [Editor\_RunMacro](editor_runmacro) | 運行一個巨集。 |
| [Editor\_SaveFileA](editor_savefilea) | 儲存文字到一個指定的檔案中 (ANSI)。 |
| [Editor\_SaveFileW](editor_savefilew) | 儲存文字到一個指定的檔案中 (Unicode)。 |
| [Editor\_SaveTemp](editor_savetemp) | 儲存臨時文字。 |
| [Editor\_SerialToLogical](editor_serialtological) | 把序列位置轉換為邏輯坐標。 |
| [Editor\_SetAnchorPos](editor_setanchorpos) | 設置選區的原點。 |
| [Editor\_SetCaretPos](editor_setcaretpos) | 指定游標位置。 |
| [Editor\_SetCaretPosEx](editor_setcaretposex) | 移動游標位置并且選擇性地延伸選區。 |
| [Editor\_SetCell](editor_setcell) | 在指定的儲存格中設置文字。 |
| [Editor\_SetColumn](editor_setcolumn) | 設置一列文字。 |
| [Editor\_SetClipPos](editor_setclippos) | 在剪貼簿記錄上設置目前的位置。 |
| [Editor\_SetConfigA](editor_setconfiga) | 變更為一個用 ANSI 字串指定的組態。 |
| [Editor\_SetConfigW](editor_setconfigw) | 變更為一個用 Unicode 字串指定的組態。 |
| [Editor\_SetModified](editor_setmodified) | 變更文字的修改狀態。 |
| [Editor\_SetMultiSel](editor_setmultisel) | 當多個選取內容可用時，設置指定的選取內容的信息。 |
| [Editor\_SetOutlineArray](editor_setoutlinearray) | 為指定的多行設置大綱級別。 |
| [Editor\_SetOutlineLevel](editor_setoutlinelevel) | 為指定的邏輯行設置大綱級別。 |
| [Editor\_SetScrollPos](editor_setscrollpos) | 指定捲動欄位置。 |
| [Editor\_SetScrollPosEx](editor_setscrollposex) | 指定捲動欄位置。 |
| [Editor\_SetSelLength](editor_setsellength) | 變更選區的字元長度。 |
| [Editor\_SetSelType](editor_setseltype) | 設置選區狀態的類型。 |
| [Editor\_SetSelTypeEx](editor_setseltypeex) | 設置選區狀態的類型。 |
| [Editor\_SetSelView](editor_setselview) | 變更選區的開始和結束位置。 |
| [Editor\_SetStatusA](editor_setstatusa) | 在狀態列上顯示一條 ANSI 消息。 |
| [Editor\_SetStatusW](editor_setstatusw) | 在狀態列上顯示一條 Unicode 消息。 |
| [Editor\_ShowOutline](editor_showoutline) | 顯示或隱藏大綱。 |
| [Editor\_ShowTip](editor_showtip) | 顯示或隱藏工具提示。 |
| [Editor\_Sort](editor_sort) | 排序文檔。 |
| [Editor\_SplitColumn](editor_splitcolumn) | 分割目前的 CSV 文檔的指定欄。 |
| [Editor\_ToolbarClose](editor_toolbarclose) | 關閉一個自訂工具列。 |
| [Editor\_ToolbarOpen](editor_toolbaropen) | 打開自訂工具列。 |
| [Editor\_ToolbarShow](editor_toolbarshow) | 顯示或隱藏一個自訂工具列。 |
| [Editor\_Unpivot](editor_unpivot) | 通過壓平合併 CSV 數據將欄轉換為列。 |
| [Editor\_UpdateToolbar](editor_updatetoolbar) | 在工具列中更新一個按鈕的狀態。 |
| [Editor\_ViewToDev](editor_viewtodev) | 把顯示指定位置的顯示坐標轉換為設備 (客戶端) 坐標。 |
| [Editor\_ViewToLogical](editor_viewtological) | 把一個指定位置的顯示坐標轉換為邏輯坐標。 |


```{toctree}
:maxdepth: 1
editor_activatetemp
editor_addref
editor_autofill
editor_batchfindinfiles
editor_batchfindreplace
editor_batchreplaceinfiles
editor_closetemp
editor_compare
editor_convert
editor_convertcsv
editor_custombarclose
editor_custombaropen
editor_devtoview
editor_docgetconfiga
editor_docgetconfigw
editor_docgetlines
editor_docgetmodified
editor_docinfo
editor_docinfoex
editor_docsavefilea
editor_docsavefilew
editor_docsetconfiga
editor_docsetconfigw
editor_doidle
editor_editcolumn
editor_edittemp
editor_emptyundobuffer
editor_enumconfig
editor_enumhighlight
editor_execcommand
editor_execplugin
editor_extractfrequent
editor_filter
editor_finda
editor_findinfiles
editor_findinfilesa
editor_findinfilesw
editor_findregex
editor_findreplace
editor_findw
editor_free
editor_getaccelarray
editor_getactivestring
editor_getanchorpos
editor_getattr
editor_getcaretpos
editor_getcell
editor_getclip
editor_getclippos
editor_getcmdid
editor_getcolor
editor_getcolumn
editor_getconfiga
editor_getconfigw
editor_getdroppedfile
editor_getfilter
editor_getlinea
editor_getlines
editor_getlinew
editor_getmargin
editor_getmodified
editor_getmultisel
editor_getoutlinelevel
editor_getoutputstring
editor_getpagesize
editor_getredraw
editor_getref
editor_getscrollpos
editor_getselend
editor_getselstart
editor_getseltexta
editor_getseltextw
editor_getseltype
editor_getseltypeex
editor_getstatusa
editor_getstatusw
editor_getunicodename
editor_getversion
editor_getword
editor_help
editor_info
editor_inserta
editor_insertclip
editor_insertfilea
editor_insertfilew
editor_insertstringa
editor_insertstringw
editor_insertw
editor_ischarhalforfull
editor_join
editor_keyboardprop
editor_linefromchar
editor_lineindex
editor_loadconfiga
editor_loadconfigw
editor_loadfilea
editor_loadfilew
editor_logicaltoserial
editor_logicaltoview
editor_manageduplicates
editor_matchregex
editor_numbering
editor_outputdir
editor_outputstring
editor_overwritea
editor_overwritew
editor_pivottable
editor_querystatus
editor_querystring
editor_querystringex
editor_rearrangecolumns
editor_redraw
editor_regqueryvalue
editor_regsetvalue
editor_release
editor_removeclip
editor_replacea
editor_replaceinfiles
editor_replaceinfilesa
editor_replaceinfilesw
editor_replacew
editor_rotateclip
editor_runmacro
editor_savefilea
editor_savefilew
editor_savetemp
editor_serialtological
editor_setanchorpos
editor_setcaretpos
editor_setcaretposex
editor_setcell
editor_setclippos
editor_setcolumn
editor_setconfiga
editor_setconfigw
editor_setmodified
editor_setmultisel
editor_setoutlinearray
editor_setoutlinelevel
editor_setscrollpos
editor_setscrollposex
editor_setsellength
editor_setseltype
editor_setseltypeex
editor_setselview
editor_setstatusa
editor_setstatusw
editor_showoutline
editor_showtip
editor_sort
editor_splitcolumn
editor_toolbarclose
editor_toolbaropen
editor_toolbarshow
editor_unpivot
editor_updatetoolbar
editor_viewtodev
editor_viewtological
```
