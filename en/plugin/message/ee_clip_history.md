# EE\_CLIP\_HISTORY

Manipulates the Clipboard history. You can send this message explicitly or by using the [Editor\_GetClip](../macro/editor_getclip), [Editor\_GetClipPos](../macro/editor_getclippos), [Editor\_InsertClip](../macro/editor_insertclip),
[Editor\_RemoveClip](../macro/editor_removeclip), [Editor\_RotateClip](../macro/editor_rotateclip), or [Editor\_SetClipPos](../macro/editor_setclippos) inline function.

```
EE_CLIP_HISTORY
wParam = 0;
lParam = (LPARAM) (CLIP_INFO) pCI;
```

## Parameters

_pTI_

Pointer to the [CLIP\_INFO](../structure/clip_info) structure.

## Return Values

If the message fails, the return value is -1. If the message succeeds, the return value depends on the value specified as the nAction parameter of the CLIP\_INFO structure. If the nAction parameter is CI\_GET\_CLIP, the return value is the size of the pszBuf buffer in characters needed to receive
the text including the terminating NULL. If the nAction parameter is CI\_INSERT\_CLIP, the return value is the position in the Clipboard history where the new text is inserted. If the nAction parameter is CI\_REMOVE\_CLIP, the return value is the position in the Clipboard history
where the text is removed. If the nAction parameter is CI\_GET\_CLIP\_POS, the return value is the current position in the Clipboard history. If the nAction parameter is CI\_SET\_CLIP\_POS, the return value is the old position in the Clipboard history. If the nAction parameter is CI\_ROTATE\_CLIP, the return value is 1.

## Version

Supported on EmEditor Version 9.00 or later.
