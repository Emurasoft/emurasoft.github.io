# EmEditor Professional和EmEditor Standard的新功能

## 新增命令

- [總是置頂 \- 開命令](../cmd/window/window_always_top_on)
- [總是置頂 \- 關命令](../cmd/window/window_always_top_off)

## 增加新選項的已存在的對話方塊

- [自訂對話方塊](../dlg/customize/index)
- [配置屬性](../dlg/properties/index) 中的 [檔案選項卡](../dlg/properties/file/index)

## 其他新增功能

- 您能在執行 [在檔案中查找 命令](../cmd/search/grep) 時終止該命令。
- 您能通過規則運算式在 [在檔案中查找 命令](../cmd/search/grep) 中用多位元字符。
- 提高了用一個規則運算式搜尋的速度。
- 優化了 EmEditor 如何搜尋其他窗口，并讓 EmEditor 的啟動更加快速。
- 添加了「說明」 鍵到每一個對話方塊中。
- 添加了更多細節來加強 EmEditor 的「說明」，包括[命令參考](../cmd/index) 以及[常見問題解答](../faq/index)。
- 在 Windows 2000/XP/2003 操作系統上，不僅是核心功能和一些對話方塊，而是所有的對話方塊都支持 Unicode。
- 添加了 /? 開關到[命令行選項](../howto/file/file_commandline) 中。
- 在預設設定下，一個被插入的字符串能通過執行一次 [撤消 命令](../cmd/edit/edit_undo) 就被撤消。這個行為能被還原到之前的行為通過在 [自訂 對話方塊](../dlg/customize/index) 中 [進階 選項卡](../dlg/customize/advanced/index) 上取消勾選逐格撤消 (需要重啟 EmEditor ) 復選框。
- 清除了自述檔案 (emeditor.txt) 并且包所有的信息整合進了「說明」中。
- 添加了新的外掛程式消息 [EE\_SET\_SEL\_TYPE](../plugin/message/ee_set_sel_type)， [EE\_GET\_STATUSA](../plugin/message/ee_get_statusa)，
[EE\_GET\_STATUSW](../plugin/message/ee_get_statusw)，
[EE\_INSERT\_FILEA](../plugin/message/ee_insert_filea)，
[EE\_INSERT\_FILEW](../plugin/message/ee_insert_filew)，
[EE\_GET\_ANCHOR\_POS](../plugin/message/ee_get_anchor_pos)，
[EE\_SET\_ANCHOR\_POS](../plugin/message/ee_set_anchor_pos)， 并用新的函數拓展了已存在的消息
[EE\_INSERT\_STRINGA](../plugin/message/ee_insert_stringa)，
[EE\_INSERT\_STRINGW](../plugin/message/ee_insert_stringw)，
[EE\_GET\_VERSION](../plugin/message/ee_get_version)，
[EE\_INFO](../plugin/message/ee_info)，
[EE\_SET\_CARET\_POS](../plugin/message/ee_set_caret_pos)。
-被另一個程序更改時 下拉列表框中的提示，自動重新載入，or保存鎖定 選項允許 EmEditor 變更只讀狀態當檔案的只讀屬性變化時。
