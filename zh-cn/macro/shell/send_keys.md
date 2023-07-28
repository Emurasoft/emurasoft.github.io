# SendKeys 方法 (Shell 对象)

发送一个或多个键击到活动窗口中（就如同在键盘上输入一样）。 这个 Send Keys 方法还能模拟鼠标活动。当这个方法发送所有鼠标操作到任何窗口中时，我们不推荐再发送鼠标操作到已经开始运行宏的 EmEditor 窗口中。

## 

### \[JavaScript\]

```
shell.SendKeys( str );
```

### \[VBScript\]

```
shell.SendKeys str
```

## 参数

_str_

指定一个表示你想要发送的击键的字符串。它还能包括鼠标活动。要发送特殊字符或鼠标活动，请用下列的表格:

|     |     |
| --- | --- |
|键 |参数 |
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
| 鼠标按下 | {BTNDOWN button, x, y} |
| 鼠标弹起 | {BTNUP button, x, y} |
| 单击鼠标 | {CLICK button, x, y} |
| 双击鼠标 | {DBLCLICK button, x, y} |
| 移动鼠标到 | {MOVETO button, x, y} |
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

x: X 屏幕坐标值

y: Y 屏幕坐标值

当按下 SHIFT 时，同时按下 A 和 B,用 "+(ab)".

当按下 SHIFT 时，同时按下 A，然后再按一个 B (这时不按 SHIFT)，用 "+ab".

## 示例

### \[JavaScript\]

```
shell.SendKeys( "{CLICK LEFT, 10 , 20}" );  // 在屏幕坐标 (10,20) 处点击鼠标左键。
shell.SendKeys( "{MOVETO, 30 , 40}" );      // 把鼠标移到屏幕坐标 (30,40) 处。
shell.SendKeys( "abc~" );                   // 输入 "abc" 并按 Enter。
shell.SendKeys( "%fo" );                    // 按住 ALT 不放的同时，按下 F，然后放开 ALT，按下 O。
shell.SendKeys( "{~}~" );                   // 输入 "~" 然后按 Enter。
shell.SendKeys( "{VK25}" );                 // 按下 KANJI 键 (VK\KANJI = 25)。
shell.SendKeys( "{VK65 DOWN}" );            // 按下 A 键，并按住不放 （A 键 = 65）。
```

### \[VBScript\]

```
shell.SendKeys "{CLICK LEFT, 10 , 20}"      // 在屏幕坐标 (10,20) 处点击鼠标左键。
shell.SendKeys "{MOVETO, 30 , 40}"          // 把鼠标移到屏幕坐标 (30,40) 处。
shell.SendKeys "abc~"                       // 输入 "abc" 并按 Enter。
shell.SendKeys "%fo"                        // 按住 ALT 不放的同时，按下 F，然后放开 ALT，按下 O。
shell.SendKeys "{~}~"                       // 输入 "~" 然后按 Enter。
shell.SendKeys "{VK25}"                     // 按下 KANJI 键 (VK\KANJI = 25)。
shell.SendKeys "{VK65 DOWN}"                // 按下 A 键，并按住不放 （A 键 = 65）。
```

## 版本

支持 EmEditor 7.00 或之后的版本。
