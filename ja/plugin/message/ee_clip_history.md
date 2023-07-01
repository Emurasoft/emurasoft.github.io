# EE\_CLIP\_HISTORY

クリップボードの履歴を操作します。このメッセージを直接送るか、または [Editor\_GetClip](../macro/editor_getclip)、 [Editor\_GetClipPos](../macro/editor_getclippos)、 [Editor\_InsertClip](../macro/editor_insertclip)、 [Editor\_RemoveClip](../macro/editor_removeclip)、 [Editor\_RotateClip](../macro/editor_rotateclip)、または
[Editor\_SetClipPos](../macro/editor_setclippos) インライン関数を使うことができます。

EE\_ADD\_REF

wParam = 0;

lParam = (LPARAM)(HINSTANCE)hInstance;

## パラメータ

_pTI_

> [CLIP\_INFO 構造体](../structure/clip_info) へのポインタを指定します。

## 戻り値

> メッセージが失敗すると、戻り値は -1 になります。メッセージが成功すると、戻り値はCLIP\_INFO 構造体の nAction パラメータとして指定した値に依存します。nAction パラメータが CI\_GET\_CLIP の場合、戻り値は、テキストを受信するために必要な pszBuf バッファの終端 NULL 文字を含めた文字単位のサイズになります。nAction パラメータが
> CI\_INSERT\_CLIP の場合、戻り値は、新しいテキストが入力されたクリップボード履歴の位置なります。nAction パラメーターが CI\_REMOVE\_CLIP の場合、戻り値は、テキストが削除されたクリップボード履歴の位置になります。nAction パラメータが CI\_GET\_CLIP\_POS の場合、戻り値はクリップボード履歴の現在の位置になります。もし nAction パラメータが CI\_SET\_CLIP\_POS の場合、戻り値はクリップボード履歴の古い位置になります。もし
> nAction パラメーターが CI\_ROTATE\_CLIP の場合、戻り値は 1 になります。

## バージョン

> Version 9.00 以上で利用できます。
