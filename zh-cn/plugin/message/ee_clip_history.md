# EE\_CLIP\_HISTORY

操控剪贴板记录。你能明确地发送该消息或用 [Editor\_GetClip](../macro/editor_getclip)， [Editor\_GetClipPos](../macro/editor_getclippos)， [Editor\_InsertClip](../macro/editor_insertclip)，
[Editor\_RemoveClip](../macro/editor_removeclip)， [Editor\_RotateClip](../macro/editor_rotateclip)，或 [Editor\_SetClipPos](../macro/editor_setclippos) 内联函数。

```
EE_CLIP_HISTORY
wParam = 0;
lParam = (LPARAM) (CLIP_INFO) pCI;
```

## 参数

_pTI_

指针指向 [CLIP\_INFO](../structure/clip_info) 结构。

## 返回值

如果消息没有成功发送，那么返回值是 -1。如果消息发送成功，那么返回值取决于 CLIP\_INFO 结构的 nAction 参数所指定的值。如果 nAction 参数是 CI\_GET\_CLIP，那么返回值则是以字节数表示的 pszBuf 缓冲区大小，这个缓冲区被用来需要包括终止空字符的文本。如果 nAction 参数是 CI\_INSERT\_CLIP，那返回值是剪贴板记录中新文本被插入的位置。如果 nAction 参数是 CI\_REMOVE\_CLIP，那返回值便是剪贴板记录中文本被删除的位置。如果 nAction 参数是 CI\_GET\_CLIP\_POS，那返回值是剪贴板记录中的当前位置。如果 nAction 参数是 CI\_SET\_CLIP\_POS，那返回值是剪贴板记录中的旧位置。如果 nAction 参数是 CI\_ROTATE\_CLIP，那返回值是 1。

## 支持版本

支持 EmEditor 9.00 或之后的版本。
