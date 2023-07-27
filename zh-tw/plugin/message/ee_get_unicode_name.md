# EE\_GET\_UNICODE\_NAME

檢索指定字元或字串的 Unicode 名。你能明確地發送該消息或用 [Editor\_GetUnicodeName 內嵌函式](../macro/editor_getunicodename)。

EE\_GET\_UNICODE\_NAME

wParam = (WPARAM)(UNICODE\_NAME\_INFO\*)pUNI;

lParam = 0;

## 參數

_pUNI_

指定指針指向 [UNICODE\_NAME\_INFO 結構](../structure/unicode_name_info)。

## 返回值

如果 UNICODE\_NAME\_INFO 結構的 _cchBuf_ 欄位是零，那返回值則是用字元數表示的一個會接收文字的緩衝區的必需大小。

## 版本

支持 EmEditor Professional 19.1 或之後的版本。
