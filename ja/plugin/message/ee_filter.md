# EE\_FILTER

指定する文字列と設定で文書にフィルターをかけます。このメッセージを直接送るか、または
[Editor\_Filter インライン関数](../macro/editor_filter) を使うことができます。

EE\_FILTER

wParam = (WPARAM) (FILTER\_INFO\_EX\*) pFilterInfo;

lParam = 0;

## パラメータ

_pFilterInfo_

[FILTER\_INFO\_EX 構造体](../structure/filter_info_ex) へのポインタを指定します。

## 戻り値

戻り値は、指定する文字列に一致する行数になります。指定文字列が空で、かつ FLAG\_FIND\_BOOKMARKED\_ONLY、FLAG\_FIND\_UNBOOKMARKED\_ONLY、FLAG\_FIND\_MATCH\_NL のいずれも指定されていない場合、戻り値は -1 になります。eeFindContinue が指定されている場合、戻り値は 0 になります。

## バージョン

Version 14.7 以上で利用できます。
