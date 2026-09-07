# Editor\_GetTextW

文書のテキストを取得します。文書に含まれる UTF-16 文字が `0x7ffffffe` 文字を超える場合、このテキストはその長さに切り詰められます。このインライン関数を使うか、または
[EE\_GET\_TEXTW メッセージ](../message/ee_get_textw) を直接送ることができます。

Editor\_GetTextW( HWND hwnd, UINT\_PTR nBufferSize, LPWSTR szBuffer );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nBufferSize_

テキストを取得するバッファのサイズを文字単位で指定します。文字列終端のヌル文字を含めます。

_szBuffer_

テキストを取得するバッファへのポインタを指定します。

## 戻り値

文書に `0x7ffffffe` を超える UTF-16 コード単位が含まれている場合、戻り値は `0x7fffffff` になります。エラーが発生した場合は 0 を返します。
