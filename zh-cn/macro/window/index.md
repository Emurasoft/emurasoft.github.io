# Window 对象

## 属性

|     |     |
| --- | --- |
| **[Caption](caption)** | 返回窗口的描述文字。 |
| **[Children](children)** | 返回代表子窗口的 Windows 集合。. |
| **[ClassName](class_name)** | 返回窗口的类名。 |
| **[clipboardData](clipboarddata)** | 返回 clipboardData 对象。 |
| **[CombineHistory](combine_history)** | 指定要不要合并撤消/重做记录。 |
| **[DiscardUndo](discard_undo)** | 返回标志来表示 EmEditor 要是否丢弃撤消信息以提高替换、插入或删除的速度。 |
| **[document](window_document)** | 返回 Document 对象。 |
| [**DroppedFiles**](droppedfiles) | 返回 DroppedFiles 对象。 |
| **[editor](window_editor)** | 返回 Editor 对象。 |
| **[Enabled](enabled)** | 返回是否窗口启用了鼠标和键盘输入。 |
| [**ExStyle**](exstyle) | 返回指定窗口的扩展样式。 |
| **[Height](height)** | 返回或设置窗口高度。 |
| **[hWnd](hwnd)** | 检索或设置窗口的句柄值。 |
| [**Interface**](interface) | 返回 Interface 对象。 |
| **[LeftX](leftx)** | 以像素为单位返回或设置指定窗口的水平位置。 |
| **[OutputBar](output_bar)** | 返回 OutputBar 对象。 |
| **[Parent](parent)** | 返回父窗口对象。 |
| **[ProcessID](process_id)** | 返回进程标识符。 |
| **[Redraw](window_redraw)** | 在 EmEditor 中允许或禁止重绘变更。 |
| **[ScriptFullName](scriptfullname)** | 检索当前运行的宏文件的完整路径以及文件名称。 |
| **[ScriptName](scriptname)** | 仅检索当前运行的宏文件的文件名。 |
| [**Style**](style) | 返回指定窗口的样式。 |
| **[scrollX](window_scrollx)** | 返回滚动栏的水平位置。 |
| **[scrollY](window_scrolly)** | 返回滚动栏的垂直位置。 |
| **[shell](shell)** | 返回 Shell 对象。 |
| **[status](window_status)** | 检索或设置在状态栏上显示的一个字符串。 |
| **[ThreadID](thread_id)** | 返回创建窗口的线程的标识符。 |
| **[Top](top)** | 以像素为单位返回或设置指定窗口的垂直位置。 |
| **[Valid](valid)** | 返回是否窗口句柄还有效。 |
| **[Visible](visible)** | 返回是否窗口可见。 |
| **[Width](width)** | 返回或设置窗口的宽度。 |

## 方法

|     |     |
| --- | --- |
| **[alert](window_alert)** | 在一个简单的对话框中显示一条消息和「OK」按钮。 |
| **[close](window_close)** | 关闭窗口。 |
| **[confirm](window_confirm)** | 在一个简单的对话框内显示一条消息以及「OK」和「Cancel」按钮。 |
| **[CreatePopupMenu](createpopupmenu)** | 创建一个弹出菜单。 |
| **[FindWindow](find_window)** | 通过类名和/或一个窗口标题查找子 Window 对象。 |
| **[FindWindowByID](find_window_by_id)** | 通过窗口标识符查找子 Window 对象。 |
| **[print](window_print)** | 显示“打印”对话框。 |
| **[prompt](window_prompt)** | 显示一个对话框来输入字符串。 |
| **[Quit](quit)** | 终止执行宏。 |
| **[scrollBy](window_scrollby)** | 通过指定的相对量滚动窗口。 |
| **[scrollTo](window_scrollto)** | 把窗口滚动至指定的位置。 |
| **[SetFocus](set_focus)** | 把键盘焦点设置到该窗口中。 |
| **[SetForeground](set_foreground)** | 将窗口置前。 |
| **[SetPosition](set_position)** | 设置窗口的大小和位置。 |
| **[ShowTip](show_tip)** | 显示工具提示。 |
| **[Sleep](window_sleep)** | 在以毫秒为单位的指定时间内暂停执行宏。 |

## 版本

支持 EmEditor 4.00 或之后的版本。

```{toctree}
:maxdepth: 1
caption
children
class_name
clipboarddata
combine_history
createpopupmenu
discard_undo
droppedfiles
enabled
exstyle
find_window
find_window_by_id
height
hwnd
interface
leftx
output_bar
parent
process_id
quit
scriptfullname
scriptname
set_focus
set_foreground
set_position
shell
show_tip
style
thread_id
top
valid
visible
width
window_alert
window_close
window_confirm
window_document
window_editor
window_print
window_prompt
window_redraw
window_scrollby
window_scrollto
window_scrollx
window_scrolly
window_sleep
window_status
```
