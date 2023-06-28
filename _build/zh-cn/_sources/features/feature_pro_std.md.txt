# EmEditor Professional 和 EmEditor Standard 的新功能

## 新增命令

- [总是置顶 \- 开命令](../cmd/window/window_always_top_on)
- [总是置顶 \- 关命令](../cmd/window/window_always_top_off)

## 增加新选项的已存在的对话框

- [自定义对话框](../dlg/customize/index)
- [配置属性](../dlg/properties/index) 中的 [文件页面](../dlg/properties/file/index)

## 其他新增功能

- 你能在执行 [**在文件中查找** 命令](../cmd/search/grep) 时终止该命令。
- 你能通过正则表达式在 [**在文件中查找** 命令](../cmd/search/grep) 中用多字节字符。
- 提高了用一个正则表达式搜索的速度。
- 优化了 EmEditor 如何搜索其他窗口，并让 EmEditor 的启动更加快速。
- 添加了 **「帮助」** 键到每一个对话框中。
- 添加了更多细节来加强 EmEditor 的“帮助”，包括 **[命令参考](../cmd/index)** 以及 **[常见问题解答](../faq/index)**。
- 在 Windows 2000/XP/2003 操作系统上，不仅是核心功能和一些对话框，而是所有的对话框都支持 Unicode。
- 添加了 /? 开关到 **[命令行选项](../howto/file/file_commandline)** 中。
- 在默认设定下，一个被插入的字符串能通过执行一次 [**撤消** 命令](../cmd/edit/edit_undo) 就被撤消。这个行为能被还原到之前的行为通过在 [**自定义** 对话框](../dlg/customize/index) 中 [**高级** 页面](../dlg/customize/advanced/index) 上取消勾选 **逐格撤消（需要重启 EmEditor ）** 复选框。
- 清除了自述文件（emeditor.txt）并且包所有的信息整合进了“帮助”中。
- 添加了新的插件消息 [EE\_SET\_SEL\_TYPE](../plugin/message/ee_set_sel_type)， [EE\_GET\_STATUSA](../plugin/message/ee_get_statusa)，
[EE\_GET\_STATUSW](../plugin/message/ee_get_statusw)，
[EE\_INSERT\_FILEA](../plugin/message/ee_insert_filea)，
[EE\_INSERT\_FILEW](../plugin/message/ee_insert_filew)，
[EE\_GET\_ANCHOR\_POS](../plugin/message/ee_get_anchor_pos)，
[EE\_SET\_ANCHOR\_POS](../plugin/message/ee_set_anchor_pos)， 并用新的函数拓展了已存在的消息
[EE\_INSERT\_STRINGA](../plugin/message/ee_insert_stringa)，
[EE\_INSERT\_STRINGW](../plugin/message/ee_insert_stringw)，
[EE\_GET\_VERSION](../plugin/message/ee_get_version)，
[EE\_INFO](../plugin/message/ee_info)，
[EE\_SET\_CARET\_POS](../plugin/message/ee_set_caret_pos)。
- **被另一个程序更改时** 下拉列表框中的 **提示**， **自动重新载入**，或 **保存锁定** 选项允许 EmEditor 变更只读状态当文件的只读属性变化时。