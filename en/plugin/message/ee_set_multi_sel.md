# EE\_SET\_MULTI\_SEL

Sets the information of a specified selection when multiple selections
are available. You can send this message
explicitly or use the [Editor\_SetMultiSel](../macro/editor_setmultisel) inline function.

EE\_SET\_MULTI\_SEL

wParam = (WPARAM) (UINT\_PTR) iSel;

lParam = (LPARAM) (const SEL\_INFO\*) pSelInfo;

## Parameters

_iSel_

> Index of the selection of which the information will be set.

_pSelInfo_

> Pointer to the
> [SEL\_INFO](../../plugin/structure/sel_info) structure.

## Return Values

> TRUE if the specified selection information is set. The
> return value is FALSE if the selection is not multiple selection mode or an
> error occurs in the function.