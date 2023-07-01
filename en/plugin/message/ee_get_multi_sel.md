# EE\_GET\_MULTI\_SEL

Retrieves the information of a specified selection when multiple selections
are available. You can send this message
explicitly or use the [Editor\_GetMultiSel](../macro/editor_getmultisel) inline function.

EE\_GET\_MULTI\_SEL

wParam = (WPARAM) (UINT\_PTR) iSel;

lParam = (LPARAM) (SEL\_INFO\*) pSelInfo;

## Parameters

_iSel_

> Index of the selection of which the information will be retrieved. If -1 is
> specified, the number of selections will be returned.

_pSelInfo_

> Pointer to the
> [SEL\_INFO](../../plugin/structure/sel_info) structure.

## Return Values

> If _iSel_ is -1, the return value is the number of selection.
> Otherwise, TRUE if the specified selection information is retrieved. The
> return value is FALSE if the selection is not multiple selection mode or an
> error occurs in the function.
