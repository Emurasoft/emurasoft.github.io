# EE\_GET\_FILTER

現在の文書にかけられているフィルターの文字列と設定を取得します。このメッセージを直接送るか、または
[Editor\_GetFilter インライン関数](../macro/editor_getfilter) を使うことができます。

EE\_GET\_FILTER

wParam = (WPARAM) (FILTER\_INFO\_EX\*) pFilterInfo;

lParam = (LPARAM)(int)iFilter;

## パラメータ

_pFilterInfo_

> [FILTER\_INFO\_EX 構造体](../structure/filter_info_ex) へのポインタを指定します。

_iFilter_

> 文字列や設定を取得したいフィルターのインデックスを指定するか、またはフィルターの数を取得するには -1 を指定します。

## 戻り値

> iFilter が 0 以上でメッセージが成功すると、戻り値は TRUE になります。iFilter が -1 の場合、戻り値はフィルターの数になります。