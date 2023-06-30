# SendKeys Method (Shell Object)

Sends one or more keystrokes to the active window (as if typed on the keyboard). The Send Keys method can also emulate mouse activities. While this method can send all mouse operation to any windows, it is not recommended to send mouse operations
to the same EmEditor window where the macro is started.

#### \[JavaScript\]

shell. **SendKeys**( _str_ );

#### \[VBScript\]

shell. **SendKeys** _str_

## Parameters

_str_

Specifies a string indicating the keystrokes you want to send. It can also include the mouse activities. To send special characters or mouse activities, use the following table:

|     |     |
| --- | --- |
| **Key** | **Parameter** |
| ALT | % |
| ALT DOWN | {ALT DOWN} |
| ALT UP | {ALT UP} |
| APPS | {APPS} |
| BACKSPACE | {BACKSPACE}, {BS}, or {BKSP} |
| BREAK | {BREAK} |
| CAPS LOCK | {CAPSLOCK} |
| CLEAR | {CLEAR} |
| CTRL | ^ |
| CTRL DOWN | {CTRL DOWN} |
| CTRL UP | {CTRL UP} |
| CONVERT | {CONVERT} |
| DEL or DELETE | {DELETE} or {DEL} |
| DOWN ARROW | {DOWN} |
| END | {END} |
| ENTER | {ENTER} or ~ |
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
| INS or INSERT | {INSERT} or {INS} |
| LEFT ARROW | {LEFT} |
| LEFT WINDOWS | {LWIN} |
| Mouse Down | {BTNDOWN button, x, y} |
| Mouse Up | {BTNUP button, x, y} |
| Mouse Click | {CLICK button, x, y} |
| Mouse Double-click | {DBLCLICK button, x, y} |
| Mouse Move To | {MOVETO, x, y} |
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

x: X screen coordinate value

y: Y screen coordinate value

When the SHIFT is held down while both A and B are pressed, use "+(ab)".

When the SHIFT is held down while A is pressed, followed by a lone B (with no SHIFT), use "+ab".

## Examples

#### \[JavaScript\]

shell.SendKeys( "{CLICK LEFT, 10 , 20}" );  // Click Left Mouse Button at screen coordinate (10,20).

shell.SendKeys( "{MOVETO, 30 , 40}" );      // Move Mouse to screen coordinate (30,40).

shell.SendKeys( "abc~" );                   // Type "abc" and then press Enter.

shell.SendKeys( "%fo" );                    // While ALT is held down, press F, and then press O without ALT.

shell.SendKeys( "{~}~" );                   // Type "~" and then press Enter.

shell.SendKeys( "{VK25}" );                 // Press the KANJI key (VK\_KANJI = 25).

shell.SendKeys( "{VK65 DOWN}" );            // Press the A key, and hold it down (A key = 65).

#### \[VBScript\]

shell.SendKeys "{CLICK LEFT, 10 , 20}"      // Click Left Mouse Button at screen coordinate (10,20).

shell.SendKeys "{MOVETO, 30 , 40}"          // Move Mouse to screen coordinate (30,40).

shell.SendKeys "abc~"                       // Type "abc" and then press Enter.

shell.SendKeys "%fo"                        // While ALT is held down, press F, and then press O without ALT.

shell.SendKeys "{~}~"                       // Type "~" and then press Enter.

shell.SendKeys "{VK25}"                     // Press the KANJI key (VK\_KANJI = 25).

shell.SendKeys "{VK65 DOWN}"                // Press the A key, and hold it down (A key = 65).

## Version

Supported on EmEditor Professional Version 7.00 or later.