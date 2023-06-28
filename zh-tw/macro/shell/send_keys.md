# SendKeys 方法

發送一個或多個鍵擊到活動視窗中 (就如同在鍵盤上輸入一樣) 。 這個 Send Keys 方法還能模擬游標活動。當這個方法發送所有游標操作到任何視窗中時，我們不推薦再發送游標操作到已經開始運行巨集的 EmEditor 視窗中。

#### \[JavaScript\]

shell. **SendKeys**( _str_ );

#### \[VBScript\]

shell. **SendKeys** _str_

## 參數

_str_

指定一個表示您想要發送的擊鍵的字串。它還能包括游標活動。要發送特殊字元或游標活動，請用下列的表格:

|     |     |
| --- | --- |
| **鍵** | **參數** |
| ALT | % |
| ALT DOWN | {ALT DOWN} |
| ALT UP | {ALT UP} |
| APPS | {APPS} |
| BACKSPACE | {BACKSPACE}，{BS}，或 {BKSP} |
| BREAK | {BREAK} |
| CAPS LOCK | {CAPSLOCK} |
| CLEAR | {CLEAR} |
| CTRL | ^ |
| CTRL DOWN | {CTRL DOWN} |
| CTRL UP | {CTRL UP} |
| CONVERT | {CONVERT} |
| DEL 或 DELETE | {DELETE} 或 {DEL} |
| DOWN ARROW | {DOWN} |
| END | {END} |
| ENTER | {ENTER} 或 ~ |
| ESC | {ESC} |
| F1 | {F1} |
| F2 | {F2} |
| F3 | {F3} |
| F4 | {F4} |
| F5 | {F5} |
| F6 | {F6} |
| F7 | {F7} |
| F8 | {F8} |
| F9 | {F9} |
| F10 | {F10} |
| F11 | {F11} |
| F12 | {F12} |
| F13 | {F13} |
| F14 | {F14} |
| F15 | {F15} |
| F16 | {F16} |
| HELP | {HELP} |
| HOME | {HOME} |
| INS 或 INSERT | {INSERT} 或 {INS} |
| LEFT ARROW | {LEFT} |
| LEFT WINDOWS | {LWIN} |
| 滑鼠按下 | {BTNDOWN button, x, y} |
| 滑鼠彈起 | {BTNUP button, x, y} |
| 單擊滑鼠 | {CLICK button, x, y} |
| 雙擊滑鼠 | {DBLCLICK button, x, y} |
| 移動滑鼠到 | {MOVETO button, x, y} |
| NONCONVERT | {NONCONVERT} |
| NUM LOCK | {NUMLOCK} |
| NUMPAD \* | {NUMPAD\*} |
| NUMPAD + | {NUMPAD+} |
| NUMPAD - | {NUMPAD-} |
| NUMPAD . | {NUMPAD.} |
| NUMPAD / | {NUMPAD/} |
| NUMPAD 0 | {NUMPAD0} |
| NUMPAD 1 | {NUMPAD1} |
| NUMPAD 2 | {NUMPAD2} |
| NUMPAD 3 | {NUMPAD3} |
| NUMPAD 4 | {NUMPAD4} |
| NUMPAD 5 | {NUMPAD5} |
| NUMPAD 6 | {NUMPAD6} |
| NUMPAD 7 | {NUMPAD7} |
| NUMPAD 8 | {NUMPAD8} |
| NUMPAD 9 | {NUMPAD9} |
| PAGE DOWN | {PGDN} |
| PAGE UP | {PGUP} |
| PRINT SCREEN | {PRTSC} |
| RIGHT ARROW | {RIGHT} |
| RIGHT WINDOWS | {RWIN} |
| SCROLL LOCK | {SCROLLLOCK} |
| SHIFT | + |
| SHIFT DOWN | {SHIFT DOWN} |
| SHIFT UP | {SHIFT UP} |
| TAB | {TAB} |
| UP ARROW | {UP} |
| [Virtual-Key Code](https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes) #nnn | {VKnnn} |

button: LEFT, RIGHT, MIDDLE

x: X 屏幕坐標值

y: Y 屏幕坐標值

當按下 SHIFT 時，同時按下 A 和 B,用 "+(ab)".

當按下 SHIFT 時，同時按下 A，然後再按一個 B (這時不按 SHIFT)，用 "+ab".

## 範例

#### \[JavaScript\]

shell.SendKeys( "{CLICK LEFT, 10 , 20}" );  // 在屏幕座標 (10,20) 處點擊滑鼠左鍵。

shell.SendKeys( "{MOVETO, 30 , 40}" );      // 把滑鼠移到屏幕座標 (30,40) 處。

shell.SendKeys( "abc~" );                   // 輸入 "abc" 並按 Enter。

shell.SendKeys( "%fo" );                    // 按住 ALT 不放的同時，按下 F，然後放開 ALT，按下 O。

shell.SendKeys( "{~}~" );                   // 輸入 "~" 然後按 Enter。

shell.SendKeys( "{VK25}" );                 // 按下 KANJI 鍵 (VK\_KANJI = 25)。

shell.SendKeys( "{VK65 DOWN}" );            // 按下 A 鍵，並按住不放 （A 鍵 = 65）。

#### \[VBScript\]

shell.SendKeys "{CLICK LEFT, 10 , 20}"      // 在屏幕座標 (10,20) 處點擊滑鼠左鍵。

shell.SendKeys "{MOVETO, 30 , 40}"          // 把滑鼠移到屏幕座標 (30,40) 處。

shell.SendKeys "abc~"                       // 輸入 "abc" 並按 Enter。

shell.SendKeys "%fo"                        // 按住 ALT 不放的同時，按下 F，然後放開 ALT，按下 O。

shell.SendKeys "{~}~"                       // 輸入 "~" 然後按 Enter。

shell.SendKeys "{VK25}"                     // 按下 KANJI 鍵 (VK\_KANJI = 25)。

shell.SendKeys "{VK65 DOWN}"                // 按下 A 鍵，並按住不放 （A 鍵 = 65）。

## 版本

支持 EmEditor 7.00 或之後的版本。