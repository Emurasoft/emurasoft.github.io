# SendKeys メソッド (Shell オブジェクト)

アクティブなウィンドウに （キーボードをタイプしているかのように） にキー ストロークを送ります。また、Send Keys メソッドはマウス アクティブティも模倣することができます。このメソッドは、どのウィンドウにもマウス操作を送ることができますが、マクロを開始した EmEditor ウィンドウにマウス操作を送ることは推奨しません。

## 

### \[JavaScript\]

```
shell.SendKeys( str );
```

### \[VBScript\]

```
shell.SendKeys str
```

## パラメータ

_str_

送りたいキー ストロークを示す文字列を指定します。マウス アクティブティも含みます。特殊文字やマウス アクティブティを送るには、以下の表を参照してください。

|     |     |
| --- | --- |
|Key |Parameter |
| ALT | % |
| ALT 下 | {ALT DOWN} |
| ALT 上 | {ALT UP} |
| APPS | {APPS} |
| BACKSPACE | {BACKSPACE}, {BS}, または {BKSP} |
| BREAK | {BREAK} |
| CAPS LOCK | {CAPSLOCK} |
| CLEAR | {CLEAR} |
| CTRL | ^ |
| CTRL 下 | {CTRL DOWN} |
| CTRL 上 | {CTRL UP} |
| 変換 | {CONVERT} |
| DEL または DELETE | {DELETE} または {DEL} |
| 下矢印 | {DOWN} |
| END | {END} |
| ENTER | {ENTER} または ~ |
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
| INS または INSERT | {INSERT} または {INS} |
| 左矢印 | {LEFT} |
| 左 WINDOWS | {LWIN} |
| マウス下 | {BTNDOWN button, x, y} |
| マウス上 | {BTNUP button, x, y} |
| マウス クリック | {CLICK button, x, y} |
| マウス ダブルクリック | {DBLCLICK button, x, y} |
| マウス移動 | {MOVETO, x, y} |
| 無変換 | {NONCONVERT} |
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
| 右矢印 | {RIGHT} |
| 右 WINDOWS | {RWIN} |
| SCROLL LOCK | {SCROLLLOCK} |
| SHIFT | + |
| SHIFT 下 | {SHIFT DOWN} |
| SHIFT 上 | {SHIFT UP} |
| TAB | {TAB} |
| 上矢印 | {UP} |
| [仮想キー コード](https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes) #nnn | {VKnnn} |

button: LEFT, RIGHT, MIDDLE

x: X スクリーン座標値

y: Y スクリーン座標値

Shift を押しながら A と B を押すには、"+(ab)" を使用します。

Shift を押しながら A を押して、そのあと Shift を押さないで B だけを押すには、 "+ab" を使用します。

## 例

### \[JavaScript\]

```
shell.SendKeys( "{CLICK LEFT, 10 , 20}" );  // スクリーン座標 (10,20) で、マウスの左ボタンｎをクリックします。
shell.SendKeys( "{MOVETO, 30 , 40}" );      // マウスをスクリーン座標 (30,40) に移動します。
shell.SendKeys( "abc~" );                   // "abc" と入力して Enter を押します。
shell.SendKeys( "%fo" );                    // Alt を押しながら F を押し、その後 Alt を押さないで O を押します 。
shell.SendKeys( "{~}~" );                   // "~" と入力して Enter を押します。
shell.SendKeys( "{VK25}" );                 // 漢字キーを押します (VK\KANJI = 25)。
shell.SendKeys( "{VK65 DOWN}" );            // A キーを押し続けます (A キー = 65)。
```

### \[VBScript\]

```
shell.SendKeys "{CLICK LEFT, 10 , 20}"      // スクリーン座標 (10,20) で、マウスの左ボタンｎをクリックします。
shell.SendKeys "{MOVETO, 30 , 40}"          // マウスをスクリーン座標 (30,40) に移動します。
shell.SendKeys "abc~"                       // "abc" と入力して Enter を押します。
shell.SendKeys "%fo"                        // Alt を押しながら F を押し、その後 Alt を押さないで O を押します 。
shell.SendKeys "{~}~"                       // "~" と入力して Enter を押します。
shell.SendKeys "{VK25}"                     // 漢字キーを押します (VK\KANJI = 25)。
shell.SendKeys "{VK65 DOWN}"                // A キーを押し続けます (A キー = 65)。
```

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
