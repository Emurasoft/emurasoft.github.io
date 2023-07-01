# EE\_GET\_COLUMN

CSV モードで指定する列に文字列を取得します。このメッセージを直接送るか、または
[Editor\_GetColumn](../macro/editor_getcolumn) インライン関数を使うことができます。

EE\_GET\_COLUMN

wParam = (WPARAM) 0;

lParam = (LPARAM) (COLUMN\_STRUCT\*) pColumnStruct;

## パラメータ

_pColumnStruct_

> [COLUMN\_STRUCT](../structure/column_struct) 構造体へのポインタを指定します。

## 戻り値

> 成功すると、テキストを取得するのに必要なバッファのサイズを終端 Null 文字を含めて文字単位で返します。失敗すると負の値になります。戻り値は、テキストを取得するのに必要な正確な値より大きくなることがあります。
