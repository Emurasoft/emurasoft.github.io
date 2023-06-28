# Window 對象

## 屬性

|     |     |
| --- | --- |
| **[Caption](caption)** | 返回視窗的描述文字。 |
| **[Children](children)** | 返回代表子視窗的 Windows 集合。. |
| **[ClassName](class_name)** | 返回視窗的類名。 |
| **[clipboardData](clipboarddata)** | 返回 clipboardData 對象。 |
| **[CombineHistory](combine_history)** | 指定要不要合併復原/重做記錄。 |
| **[DiscardUndo](discard_undo)** | 返回標志來表示 EmEditor 要是否丟棄撤銷信息以提高取代、插入或刪除的速度。 |
| **[document](window_document)** | 返回 Document 對象。 |
| [**DroppedFiles**](droppedfiles) | 返回 DroppedFiles 對象。 |
| **[editor](window_editor)** | 返回 Editor 對象。 |
| **[Enabled](enabled)** | 返回是否視窗啟用了游標和鍵盤輸入。 |
| [**ExStyle**](exstyle) | 返回指定視窗的延伸樣式。 |
| **[Height](height)** | 返回或設置視窗高度。 |
| **[hWnd](hwnd)** | 檢索或設置視窗的句柄值。 |
| [**Interface**](interface) | 返回 Interface 對象。 |
| **[LeftX](leftx)** | 以像素為單位返回或設置指定視窗的水平位置。 |
| **[OutputBar](output_bar)** | 返回 OutputBar 對象。 |
| **[Parent](parent)** | 返回父視窗對象。 |
| **[ProcessID](process_id)** | 返回進程標識符。 |
| **[Redraw](window_redraw)** | 在 EmEditor 中允許或禁止重繪變更。 |
| **[ScriptFullName](scriptfullname)** | 檢索目前的運行的巨集檔案的完整路徑以及檔案名稱。 |
| **[ScriptName](scriptname)** | 僅檢索目前的運行的巨集檔案的檔案名。 |
| [**Style**](style) | 返回指定視窗的樣式。 |
| **[scrollX](window_scrollx)** | 返回捲軸的水平位置。 |
| **[scrollY](window_scrolly)** | 返回捲軸的垂直位置。 |
| **[shell](shell)** | 返回 Shell 對象。 |
| **[status](window_status)** | 檢索或設置在狀態列上顯示的一個字串。 |
| **[ThreadID](thread_id)** | 返回創建視窗的線程的標識符。 |
| **[Top](top)** | 以像素為單位返回或設置指定視窗的垂直位置。 |
| **[Valid](valid)** | 返回是否視窗句柄還有效。 |
| **[Visible](visible)** | 返回是否視窗可見。 |
| **[Width](width)** | 返回或設置視窗的寬度。 |

## 方法

|     |     |
| --- | --- |
| **[alert](window_alert)** | 在一個簡單的對話方塊中顯示一條消息和「OK」按鈕。 |
| **[close](window_close)** | 關閉視窗。 |
| **[confirm](window_confirm)** | 在一個簡單的對話方塊內顯示一條消息以及「OK」和「Cancel」按鈕。 |
| **[CreatePopupMenu](createpopupmenu)** | 創建一個快顯功能表。 |
| **[FindWindow](find_window)** | 通過類名和/或一個視窗標題尋找子 Window 對象。 |
| **[FindWindowByID](find_window_by_id)** | 通過視窗標識符尋找子 Window 對象。 |
| **[print](window_print)** | 顯示「列印」對話方塊。 |
| **[prompt](window_prompt)** | 顯示一個對話方塊來輸入字串。 |
| **[Quit](quit)** | 終止執行巨集。 |
| **[scrollBy](window_scrollby)** | 通過指定的相對量捲動視窗。 |
| **[scrollTo](window_scrollto)** | 把視窗捲動至指定的位置。 |
| **[SetFocus](set_focus)** | 把鍵盤焦點設置到該視窗中。 |
| **[SetForeground](set_foreground)** | 將視窗置前。 |
| **[SetPosition](set_position)** | 設置視窗的大小和位置。 |
| **[ShowTip](show_tip)** | 顯示工具提示。 |
| **[Sleep](window_sleep)** | 在以毫秒為單位的指定時間內暫停執行巨集。 |

## 版本

支持 EmEditor 4.00 或之後的版本。

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
