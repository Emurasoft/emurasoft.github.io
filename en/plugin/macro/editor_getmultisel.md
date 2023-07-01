# Editor\_GetMultiSel

Retrieves the information of a specified selection when multiple selections
are available. You can use this inline function or explicitly send the [EE\_GET\_MULTI\_SEL](../message/ee_get_multi_sel) message.

Editor\_GetMultiSel( HWND hwnd, UINT\_PTR iSel, SEL\_INFO\* pSelInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iSel_

> Index of the selection of which the information will be retrieved. If -1 is
> specified, the number of selections will be returned.

_pSelInfo_

> Pointer to the
> [SEL\_INFO](../structure/sel_info) structure.

## Return Values

> If _iSel_ is -1, the return value is the number of selection.
> Otherwise, TRUE if the specified selection information is retrieved. The
> return value is FALSE if the selection is not multiple selection mode or an
> error occurs in the function.
