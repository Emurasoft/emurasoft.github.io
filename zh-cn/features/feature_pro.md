---
orphan: true
---
# EmEditor Professional 特有新功能

## 新增功能

- [功能强大丰富的宏](macro)
- [在文件中替换](replace_in_files)
- [指定一个编码在文件中查找](grep)
- [合并窗口](tab_features)

## 新增命令

- [全部关闭不保存](../cmd/file/quit_all)
- [制表位化命令](../cmd/edit/tabify)
- [非制表位化命令](../cmd/edit/untabify)
- [增加行缩进命令](../cmd/edit/indent)
- [减少行缩进命令](../cmd/edit/unindent)
- [注释命令](../cmd/edit/edit_comment)
- [取消注释命令](../cmd/edit/edit_uncomment)
- [插入变音符命令](../cmd/edit/insert_caron)
- [制表位化整个文档命令](../cmd/edit/space_to_tab)
- [移动到上次编辑位置命令](../cmd/edit/move_last_edit)
- [当前文档中的下一个书签命令](../cmd/edit/bookmark_next_within)
- [当前文档中的上一个书签命令](../cmd/edit/bookmark_prev_within)
- [在文件中替换命令](../cmd/search/replace_in_files)
- [标记命令](../cmd/view/view_marks)
- [增大字体命令](../cmd/view/increase_font_size)
- [减小字体命令](../cmd/view/decrease_font_size)
- [使用临时选项运行宏命令](../cmd/macros/macro_run_options)
- [保存宏命令](../cmd/macros/macro_save)
- [编辑宏命令](../cmd/macros/macro_edit)
- [选择宏命令](../cmd/macros/macro_select)
- [设为当前宏命令](../cmd/macros/macro_select_this)
- [自定义宏命令](../cmd/macros/customize_macro)
- [宏参考手册命令](../cmd/macros/macro_help)
- [查找宏关键字命令](../cmd/macros/macro_help_word)
- [运行宏命令](../cmd/macros/macro1)
- [启用标签页命令](../cmd/window/window_combine)
- [查找下一个 Unicode 字符命令](../cmd/search/find_next_unicode)
- [查找上一个 Unicode 字符命令](../cmd/search/find_prev_unicode)
- [取消 Unicode 高亮命令](../cmd/search/erase_unicode_hilite)

## 增加新功能的已存在的命令

- [插入锐音符命令](../cmd/edit/insert_acute)
- [插入波形符命令](../cmd/edit/insert_tilde)

## 新的对话框

- [在文件中替换对话框](../dlg/replace_in_files/index)
- [使用临时选项运行宏对话框](../dlg/macro_temp_options/index)
- [自定义宏对话框](../dlg/macro_customize/index)

## 增加新选项的已存在的对话框

- [查找对话框](../dlg/find/index)
- [替换对话框](../dlg/replace/index)
- [在文件中查找对话框](../dlg/find_in_files/index)
- [自定义对话框](../dlg/customize/index)
- [自定义托盘图标对话框](../dlg/tray/index)

## 工具栏新增按钮

- ![](../images/filesaveexit.gif)[保存并关闭命令](../cmd/file/file_save_exit)
- ![](../images/saveexitall.gif)[保存并全部关闭命令](../cmd/file/save_exit_all)
- ![](../images/nextparen.gif)[查找配对的括号命令](../cmd/edit/next_paren)
- ![](../images/duplicateline.gif)[创建当前行的副本命令](../cmd/edit/duplicate_line)
- ![](../images/insertcontrol.gif)[插入特殊字符命令](../cmd/edit/insert_control)
- ![](../images/marks.gif)[标记命令](../cmd/view/view_marks)
- ![](../images/editcomment.gif)[注释命令](../cmd/edit/edit_comment)
- ![](../images/edituncomment.gif)[取消注释命令](../cmd/edit/edit_uncomment)
- ![](../images/indent.gif)[增加行缩进命令](../cmd/edit/indent)
- ![](../images/unindent.gif)[减少行缩进命令](../cmd/edit/unindent)
- ![](../images/macrosave.gif)[保存宏命令](../cmd/macros/macro_save)
- ![](../images/macroedit.gif)[编辑宏命令](../cmd/macros/macro_edit)
- ![](../images/macroselect.gif)[选择宏命令](../cmd/macros/macro_select)
- ![](../images/windowsplithorzfix.gif)[切换水平分割命令](../cmd/window/window_split_horz_toggle)
- ![](../images/windowcombine.gif)[启用标签页命令](../cmd/window/window_combine)
- ![](../images/increasefontsize.gif)[增大字体命令](../cmd/view/increase_font_size)
- ![](../images/decreasefontsize.gif)[减小字体命令](../cmd/view/decrease_font_size)
- ![](../images/replaceinfiles.gif)[在文件中替换命令](../cmd/search/replace_in_files)
- ![](../images/bookmarkprevwithin.gif)[当前文档中的上一个书签命令](../cmd/edit/bookmark_prev_within)
- ![](../images/bookmarknextwithin.gif)[当前文档中的下一个书签命令](../cmd/edit/bookmark_next_within)

## 其他新增功能

- The [**查找** 命令](../cmd/search/edit_find) 能搜索发生换行的行如果在 [**搜索** 页面](../dlg/customize/search/index) 上勾选了 **正则表达式 "." 匹配换行符** 复选框。可搜索的换行的行数能在 **搜索正则表达式的附加行** 文本框中被定义。
- 添加了 **「替换 >>」** 按钮在 [**查找** 对话框](../dlg/find/index) 中，让你能立刻跳转至 [**替换** 对话框](../dlg/replace/index)。
- 添加了 **「\> 」按钮** 在所有搜索对话框中来浏览可用的正则表达式。
- 添加了 **仅显示文件名** 复选框在 [**在文件中查找** 对话框](../dlg/find_in_files/index) 中。
- 添加了 **更改“查找/替换”下拉列表中的字体** 复选框和 **只有当选定字体的字符集不是系统默认时才更改字体** 复选框在 [**自定义** 对话框](../dlg/customize/index) 中的 [**搜索** 页面](../dlg/customize/search/index) 上，让你能选择条件当 **查找/替换** 下拉列表中的字体被调整到当前字体时。
- 添加了一个快捷键来显示 **托盘图标** 菜单。在默认情况下，它是 ALT + CTRL + N。你也可以在 [**自定义托盘图标** 对话框](../dlg/tray/index) 中的 **模拟鼠标左键的快捷键** 文本框中自定义快捷方式。
- 添加了一个快捷键来启动一个焦点在编辑框中的 EmEditor 窗口。原先的编辑框会充满 EmEditor 内容当 EmEditor 窗口关闭时。这个快捷键的默认设定是 ALT + CTRL + X。你也可以在 [**自定义托盘图标** 对话框](../dlg/tray/index) 中的 **使用 EmEditor 抓取文本的快捷键** 文本框中自定义快捷方式。
- 当保存一个文件时，提示消息 "该文档含有 Unicode 格式的字符 ... 是否继续？" 会出现，按 **「取消」** 按钮跳至不能被转换为要保存的编码的字符，并且高亮 Unicode 字符。
- 添加了新的开关 /bk, /eh, /fu, /fn, /ko, /mf, /rc, /rd, /ri,  还有 /rw 到 [命令行选项](../howto/file/file_commandline) 中。
- 替换表达式包括小写/大小以及半角/全角转换。
- EmEditor Professional 为 Pentium 4 CPU 提供最优化的版本(你仍然可以在别的处理器上运行EmEditor Professional )。
- 敬请期待更多功能被添加到 EmEditor Professional 中。
