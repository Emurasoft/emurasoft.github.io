# EE\_EDIT\_TEMP

一時テキストを新規文書として開くか、アクティブにするか、保存するか、または閉じます。このメッセージを直接送るか、または  [Editor\_ActivateTemp](../macro/editor_activatetemp)、 [Editor\_CloseTemp](../macro/editor_closetemp)、 [Editor\_EditTemp](../macro/editor_edittemp)、または
[Editor\_SaveTemp](../macro/editor_savetemp) インライン関数を使うことができます。

EE\_EDIT\_TEMP

wParam = 0;

lParam = (LPARAM) (TEMP\_INFO) pTI;

## パラメータ

_pTI_

[TEMP\_INFO](../structure/temp_info) 構造体へのポインタを指定します。

## 戻り値

戻り値は、新規文書の ID になります。ただし、一時テキストを閉じる場合は、戻り値が使用されます。

## バージョン

Version 9.00 以上で利用できます。
