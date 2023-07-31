---
orphan: true
---
# EmEditor Professional 特有新功能

## 新增功能

- [功能強大豐富的巨集](macro)
- [多檔取代](replace_in_files)
- [指定一個編碼在檔案中查找](grep)
- [合并窗口](tab_features)

## 新增命令

- [全部關閉不保存](../cmd/file/quit_all)
- [制表位化命令](../cmd/edit/tabify)
- [非制表位化命令](../cmd/edit/untabify)
- [增加行縮進命令](../cmd/edit/indent)
- [減少行縮進命令](../cmd/edit/unindent)
- [注釋命令](../cmd/edit/edit_comment)
- [取消注釋命令](../cmd/edit/edit_uncomment)
- [插入變音符命令](../cmd/edit/insert_caron)
- [制表位化整個文檔命令](../cmd/edit/space_to_tab)
- [移動到上次編輯位置命令](../cmd/edit/move_last_edit)
- [當前文檔中的下一個書簽命令](../cmd/edit/bookmark_next_within)
- [當前文檔中的上一個書簽命令](../cmd/edit/bookmark_prev_within)
- [多檔取代命令](../cmd/search/replace_in_files)
- [標記命令](../cmd/view/view_marks)
- [增大字體命令](../cmd/view/increase_font_size)
- [減小字體命令](../cmd/view/decrease_font_size)
- [使用臨時選項運行巨集命令](../cmd/macros/macro_run_options)
- [保存巨集命令](../cmd/macros/macro_save)
- [編輯巨集命令](../cmd/macros/macro_edit)
- [選擇巨集命令](../cmd/macros/macro_select)
- [設為當前巨集命令](../cmd/macros/macro_select_this)
- [自訂巨集命令](../cmd/macros/customize_macro)
- [巨集參考手冊命令](../cmd/macros/macro_help)
- [查找巨集關鍵字命令](../cmd/macros/macro_help_word)
- [運行巨集命令](../cmd/macros/macro1)
- [啟用標簽頁命令](../cmd/window/window_combine)
- [查找下一個 Unicode 字符命令](../cmd/search/find_next_unicode)
- [查找上一個 Unicode 字符命令](../cmd/search/find_prev_unicode)
- [取消 Unicode 高亮命令](../cmd/search/erase_unicode_hilite)

## 增加新功能的已存在的命令

- [插入銳音符命令](../cmd/edit/insert_acute)
- [插入波形符命令](../cmd/edit/insert_tilde)

## 新的對話方塊

- [多檔取代對話方塊](../dlg/replace_in_files/index)
- [使用臨時選項運行巨集對話方塊](../dlg/macro_temp_options/index)
- [自訂巨集對話方塊](../dlg/macro_customize/index)

## 增加新選項的已存在的對話方塊

- [尋找對話方塊](../dlg/find/index)
- [替換對話方塊](../dlg/replace/index)
- [在檔案中查找對話方塊](../dlg/find_in_files/index)
- [自訂對話方塊](../dlg/customize/index)
- [自訂系統匣圖示對話方塊](../dlg/tray/index)

## 工具列新增按鈕

- ![](../images/filesaveexit.gif)[保存并關閉命令](../cmd/file/file_save_exit)
- ![](../images/saveexitall.gif)[保存并全部關閉命令](../cmd/file/save_exit_all)
- ![](../images/nextparen.gif)[查找配對的括號命令](../cmd/edit/next_paren)
- ![](../images/duplicateline.gif)[創建當前行的副本命令](../cmd/edit/duplicate_line)
- ![](../images/insertcontrol.gif)[插入特殊字符命令](../cmd/edit/insert_control)
- ![](../images/marks.gif)[標記命令](../cmd/view/view_marks)
- ![](../images/editcomment.gif)[注釋命令](../cmd/edit/edit_comment)
- ![](../images/edituncomment.gif)[取消注釋命令](../cmd/edit/edit_uncomment)
- ![](../images/indent.gif)[增加行縮進命令](../cmd/edit/indent)
- ![](../images/unindent.gif)[減少行縮進命令](../cmd/edit/unindent)
- ![](../images/macrosave.gif)[保存巨集命令](../cmd/macros/macro_save)
- ![](../images/macroedit.gif)[編輯巨集命令](../cmd/macros/macro_edit)
- ![](../images/macroselect.gif)[選擇巨集命令](../cmd/macros/macro_select)
- ![](../images/windowsplithorzfix.gif)[切換水平分割命令](../cmd/window/window_split_horz_toggle)
- ![](../images/windowcombine.gif)[啟用標簽頁命令](../cmd/window/window_combine)
- ![](../images/increasefontsize.gif)[增大字體命令](../cmd/view/increase_font_size)
- ![](../images/decreasefontsize.gif)[減小字體命令](../cmd/view/decrease_font_size)
- ![](../images/replaceinfiles.gif)[多檔取代命令](../cmd/search/replace_in_files)
- ![](../images/bookmarkprevwithin.gif)[當前文檔中的上一個書簽命令](../cmd/edit/bookmark_prev_within)
- ![](../images/bookmarknextwithin.gif)[當前文檔中的下一個書簽命令](../cmd/edit/bookmark_next_within)

## 其他新增功能

- The [**查找** 命令](../cmd/search/edit_find) 能搜尋發生換行的行如果在 [**搜尋** 選項卡](../dlg/customize/search/index) 上勾選了 **規則運算式 "." 匹配換行符** 復選框。可搜尋的換行的行數能在 **搜尋規則運算式的附加行** 文本框中被定義。
- 添加了 **「替換 >>」** 按鈕在 [**查找** 對話方塊](../dlg/find/index) 中，讓您能立刻跳轉至 [**替換** 對話方塊](../dlg/replace/index)。
- 添加了 **「\> 」按鈕** 在所有搜尋對話方塊中來瀏覽可用的規則運算式。
- 添加了 **僅顯示檔案名** 復選框在 [**在檔案中查找** 對話方塊](../dlg/find_in_files/index) 中。
- 添加了 **更改「查找/替換」下拉列表中的字體** 復選框和 **只有當選定字體的字符集不是系統預設時才更改字體** 復選框在 [**自訂** 對話方塊](../dlg/customize/index) 中的 [**搜尋** 選項卡](../dlg/customize/search/index) 上，讓您能選擇條件當 **查找/替換** 下拉列表中的字體被調整到當前字體時。
- 添加了一個快捷鍵來顯示 **系統匣圖示** 菜單。在預設情況下，它是 ALT + CTRL + N。您也可以在 [**自訂系統匣圖示** 對話方塊](../dlg/tray/index) 中的 **模擬鼠標左鍵的快捷鍵** 文本框中自訂快捷方式。
- 添加了一個快捷鍵來啟動一個焦點在編輯框中的 EmEditor 窗口。原先的編輯框會充滿 EmEditor 內容當 EmEditor 窗口關閉時。這個快捷鍵的預設設定是 ALT + CTRL + X。您也可以在 [**自訂系統匣圖示** 對話方塊](../dlg/tray/index) 中的 **使用 EmEditor 抓取文本的快捷鍵** 文本框中自訂快捷方式。
- 當保存一個檔案時，提示消息 "該文檔含有 Unicode 格式的字符 ... 是否繼續？" 會出現，按 **「取消」** 按鈕跳至不能被轉換為要保存的編碼的字符，并且高亮 Unicode 字符。
- 添加了新的開關 /bk, /eh, /fu, /fn, /ko, /mf, /rc, /rd, /ri,  還有 /rw 到 [命令行選項](../howto/file/file_commandline) 中。
- 替換表達式包括小寫/大小以及半角/全角轉換。
- EmEditor Professional 為 Pentium 4 CPU 提供最優化的版本(您仍然可以在別的處理器上運行EmEditor Professional )。
- 敬請期待更多功能被添加到 EmEditor Professional 中。
