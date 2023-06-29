# Editor\_SetMultiSel

Sets the information of a specified selection when multiple selections
are available. You can use this inline function or explicitly send the [EE\_SET\_MULTI\_SEL](../message/ee_set_multi_sel) message.

Editor\_SetMultiSel( HWND hwnd, UINT\_PTR iSel, const SEL\_INFO\* pSelInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iSel_

> Index of the selection of which the information will be set.

_pSelInfo_

> Pointer to the
> [SEL\_INFO](../structure/sel_info) structure.

## Return Values

> TRUE if the specified selection information is retrieved. The
> return value is FALSE if the selection is not multiple selection mode or an
> error occurs in the function.