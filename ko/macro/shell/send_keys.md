# SendKeys 메서드 (Shell 개체)

(키보드에 입력 한 것처럼) 활성 창에 하나 이상의 키 입력을 전송합니다.
Send Keys 메서드는 마우스 활동 또한 에뮬레이트 할 수 있습니다.
이 메서드가 모든 마우스 활동을 창에 전송하는 동안은 매크로가 시작되고 있는 같은 EmEditor 창에 마우스
작업을 전송하는지 않는 것이 좋습니다.

## 

### \[JavaScript\]

```
shell.SendKeys( str );
```

### \[VBScript\]

```
shell.SendKeys str
```

## 매개 변수

_str_

전송하기 원하는 키 입력을 나타내는 문자열을 지정합니다.
마우스 활동 또한 포함할 수 있습니다. 특수 문자 또는 마우스 활동을 보내려면 다음의 표를 사용하십시오:

|     |     |
| --- | --- |
| **키** | **매개 변수** |
| BACKSPACE | {BACKSPACE}, {BS}, 또는 {BKSP} |
| BREAK | {BREAK} |
| CAPS LOCK | {CAPSLOCK} |
| DEL 또는 DELETE | {DELETE} 또는 {DEL} |
| DOWN ARROW | {DOWN} |
| END | {END} |
| ENTER | {ENTER} 또는 ~ |
| ESC | {ESC} |
| HELP | {HELP} |
| HOME | {HOME} |
| INS 또는 INSERT | {INSERT} 또는 {INS} |
| LEFT ARROW | {LEFT} |
| NUM LOCK | {NUMLOCK} |
| PAGE DOWN | {PGDN} |
| PAGE UP | {PGUP} |
| PRINT SCREEN | {PRTSC} |
| RIGHT ARROW | {RIGHT} |
| SCROLL LOCK | {SCROLLLOCK} |
| TAB | {TAB} |
| UP ARROW | {UP} |
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
| ALT | % |
| ALT DOWN | {ALT DOWN} |
| ALT UP | {ALT UP} |
| CTRL | ^ |
| CTRL DOWN | {CTRL DOWN} |
| CTRL UP | {CTRL UP} |
| SHIFT | + |
| SHIFT DOWN | {SHIFT DOWN} |
| SHIFT UP | {SHIFT UP} |
| Mouse Down | {BTNDOWN button, x, y} |
| Mouse Up | {BTNUP button, x, y} |
| Mouse Click | {CLICK button, x, y} |
| Mouse Double-click | {DBLCLICK button, x, y} |
| Mouse Move To | {MOVETO button, x, y} |

button: LEFT, RIGHT, MIDDLE

x: X 화면 좌표 값

y: Y 화면 좌표 값

A 와 B 를 모두 누른 채 SHIFT를 누르면 "+(ab)"을 사용합니다.

A를 누른 채 SHIFT를 누른 후 (SHIFT 없이) B를 따로 누르면 "+ab"을 사용합니다.

## 예시

### \[JavaScript\]

```
shell.SendKeys( "{CLICK LEFT, 10 , 20}" );  //
화면 좌표 (10,20)에서 마우스 왼쪽 버튼을 클릭합니다.
shell.SendKeys( "{MOVETO, 30 , 40}" );      //
마우스를 화면 좌표 (30,40)으로 이동합니다.
shell.SendKeys( "abc~" );                   //
"abc"를 입력하고 Enter를 누릅니다.
shell.SendKeys( "%fo" );                    //
ALT를 누른 채 F를 누른 후 ALT 없이 0을 누릅니다.
```

### \[VBScript\]

```
shell.SendKeys "{CLICK LEFT, 10 , 20}"      //
화면 좌표 (10,20)에서 마우스 왼쪽 버튼을 클릭합니다.
shell.SendKeys "{MOVETO, 30 , 40}"          //
마우스를 화면 좌표 (30,40)으로 이동합니다.
shell.SendKeys "abc~"                       //
"abc" 를 입력하고 Enter를 누릅니다.
shell.SendKeys "%fo"                        //
ALT를 누른 채 F를 누른 후 ALT 없이 0을 누릅니다.
```

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
