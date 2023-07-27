# EP\_GET\_VERSION

檢索外掛程式版本。

EP\_GET\_VERSION

hwnd = hwndParent;

wParam = cb;

lParam = szVersion;

## 參數

_hwndParent_

外掛程式設置對話方塊的視窗控制代碼。

_cb_

指定要複製到緩沖區的最大字元數，包括 NULL 字元。

_szVersion_

指針指向會接收文字的緩沖區。

## 返回值

返回值是一個能接收文字的緩沖區的必需大小。
