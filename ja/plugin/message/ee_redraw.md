# EE\_REDRAW

ウィンドウの再描画を行うかどうかを指定します。このメッセージを直接送るか、または [Editor\_Redraw インライン関数](../macro/editor_redraw) を使うことができます。

```
EE_REDRAW
wParam = (WPARAM)bRedraw;
lParam = (LPARAM)0;
```

## パラメータ

_bRedraw_

FALSE を指定すると、それ以降、再び TRUE を指定して呼び出すまで、ウィンドウの再描画を行わなくなります。

## 戻り値

戻り値は利用されません。
