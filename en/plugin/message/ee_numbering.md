# EE\_NUMBERING

Inserts numbering at the cursor position or vertical selection. You can send this message explicitly or use the [Editor\_Numbering inline function](../macro/editor_numbering).

EE\_NUMBERING

wParam = (WPARAM)(NUMBERING\_INFO\*)pNI;

lParam = 0;

## Parameters

_pUNI_

> Specifies the pointer to the [NUMBERING\_INFO structure](../structure/numbering_info).

## Return Values

> The return value is 0 if succeeds.

## Version

> Supported on Version 19.1 or later.
