# EE\_CLIP\_HISTORY

操控剪貼簿記錄。您能明確地發送該消息或通過用 [Editor\_GetClip](../macro/editor_getclip)， [Editor\_GetClipPos](../macro/editor_getclippos)， [Editor\_InsertClip](../macro/editor_insertclip)，
[Editor\_RemoveClip](../macro/editor_removeclip)， [Editor\_RotateClip](../macro/editor_rotateclip)，或 [Editor\_SetClipPos](../macro/editor_setclippos) 內嵌函式。

EE\_CLIP\_HISTORY

wParam = 0;

lParam = (LPARAM) (CLIP\_INFO) pCI;

## 參數

_pTI_

指針指向 [CLIP\_INFO](../structure/clip_info) 結構。

## 返回值

如果消息沒有成功發送，那么返回值是 -1。如果消息發送成功，那么返回值取決于 CLIP\_INFO 結構的 nAction 參數所指定的值。如果 nAction 參數是 CI\_GET\_CLIP，那么返回值則是以位元數表示的 pszBuf 緩沖區大小，這個緩沖區被用來需要包括終止空字符的文本。如果 nAction 參數是 CI\_INSERT\_CLIP，那返回值是剪貼簿記錄中新文本被插入的位置。如果 nAction 參數是 CI\_REMOVE\_CLIP，那返回值便是剪貼簿記錄中文本被刪除的位置。如果 nAction 參數是 CI\_GET\_CLIP\_POS，那返回值是剪貼簿記錄中的當前位置。如果 nAction 參數是 CI\_SET\_CLIP\_POS，那返回值是剪貼簿記錄中的舊位置。如果 nAction 參數是 CI\_ROTATE\_CLIP，那返回值是 1。

## 支持版本

支持 EmEditor 9.00 或之後的版本
