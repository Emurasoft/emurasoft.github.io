# Editor\_GetColumn

CSV モードで指定する列に文字列を設定します。このインライン関数を使うか、または [EE\_GET\_COLUMN](../message/ee_get_column) メッセージを直接送ることができます。

Editor\_GetColumn( HWND hwnd, COLUMN\_STRUCT\* pColumnStruct );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pColumnStruct_

[COLUMN\_STRUCT](../structure/column_struct) 構造体へのポインタを指定します。

## 戻り値

成功すると、テキストを取得するのに必要なバッファのサイズを終端 Null 文字を含めて文字単位で返します。失敗すると負の値になります。戻り値は、テキストを取得するのに必要な正確な値より大きくなることがあります。
