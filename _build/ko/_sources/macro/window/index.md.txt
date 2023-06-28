# Window 개체

## 속성

|     |     |
| --- | --- |
| **[Caption](caption)** | 창의 캡션 텍스트를 반환합니다. |
| **[Children](children)** | 하위 창을 나타내는 Windows 컬렉션을 반환합니다. |
| **[ClassName](class_name)** | 창의 클래스 이름을 반환합니다. |
| **[clipboardData](clipboarddata)** | clipboardData 개체를 반환합니다. |
| **[document](window_document)** | Document 개체를 반환합니다. |
| [**DroppedFiles**](droppedfiles) | DroppedFiles 개체를 반환합니다. |
| **[editor](window_editor)** | Editor 개체를 반환합니다. |
| **[Enabled](enabled)** | 창이 마우스와 키보드 입력이 가능한지 여부를 반환합니다. |
| [**ExStyle**](exstyle) | 지정된 창의 확장 스타일을 반환합니다. |
| **[Height](height)** | 창의 높이를 설정하거나 반환합니다. |
| **[hWnd](hwnd)** | 창의 핸들 값을 검색하거나 설정합니다. |
| [**Interface**](interface) | Interface 개체를 반환합니다. |
| **[LeftX](leftx)** | 픽셀로 지정된 창의 수평 위치를 설정하거나 반환합니다. |
| **[OutputBar](output_bar)** | OutputBar 개체를 반환합니다. |
| **[Parent](parent)** | 상위 window 개체를 반환합니다. |
| **[ProcessID](process_id)** | 프로세스 식별자를 반환합니다. |
| **[Redraw](window_redraw)** | 다시 그려야 하는 엠에디터의 변동 사항을 허용하거나 엠에디터에 다시 그리는 것을 방지합니다. |
| **[ScriptFullName](scriptfullname)** | 현재 실행되고 있는 매크로 파일의 파일 이름과 전체 경로를 검색합니다. |
| **[ScriptName](scriptname)** | 현재 실행되고 있는 매크로 파일의 파일 이름만을 검색합니다. |
| [**Style**](style) | 지정된 창의 스타일을 반환합니다. |
| **[scrollX](window_scrollx)** | 스크롤 바의 수평 위치를 반환합니다. |
| **[scrollY](window_scrolly)** | 스크롤 바의 수직 위치를 반환합니다. |
| **[shell](shell)** | Shell 개체를 반환합니다. |
| **[status](window_status)** | 상태 표시줄에 표시되는 문자열을 검색하거나 설정합니다. |
| **[ThreadID](thread_id)** | 창을 생성한 스레드의 식별자를 반환합니다. |
| **[Top](top)** | 픽셀로 지정된 창의 수직 위치를 검색하거나 설정합니다. |
| **[Valid](valid)** | 창 핸들이 유효한지 여부를 반환합니다. |
| **[Visible](visible)** | 창이 보이는지 여부를 반환합니다. |
| **[Width](width)** | 창의 너비를 설정하거나 반환합니다. |

## 메서드

|     |     |
| --- | --- |
| **[alert](window_alert)** | OK 버튼을 가진 간단한 대화 상자에 메시지를 표시합니다. |
| **[close](window_close)** | 창을 닫습니다. |
| **[confirm](window_confirm)** | OK 버튼과 취소 버튼을 가진 간단한 대화 상자에 메시지를 표시합니다. |
| **[CreatePopupMenu](createpopupmenu)** | 팝업 메뉴를 생성합니다. |
| **[FindWindow](find_window)** | 클래스 이름 및/또는 창 제목으로 하위 Window 개체를 검색합니다. |
| **[FindWindowByID](find_window_by_id)** | 창 식별자로 하위 Window 개체를 검색합니다. |
| **[print](window_print)** | 인쇄 대화 상자를 표시합니다. |
| **[prompt](window_prompt)** | 문자열을 입력하는 대화 상자를 표시합니다. |
| **[Quit](quit)** | 매크로 실행을 종료합니다. |
| **[scrollBy](window_scrollby)** | 지정된 상대적인 양만큼 창을 스크롤합니다. |
| **[scrollTo](window_scrollto)** | 지정된 위치로 창을 스크롤합니다. |
| **[SetFocus](set_focus)** | 창에 키보드 포커스를 설정합니다. |
| **[SetForeground](set_foreground)** | 전경 창을 제공합니다. |
| **[SetPosition](set_position)** | 창의 위치와 크기를 설정합니다. |
| **[Sleep](window_sleep)** | 밀리 초 단위로 지정 된 시간만큼 매크로 실행을 일시 정지합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.

```{toctree}
:maxdepth: 1
caption
children
class_name
clipboarddata
createpopupmenu
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
