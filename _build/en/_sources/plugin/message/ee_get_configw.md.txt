# EE\_GET\_CONFIGW

檢索所選取的配置名稱為 Unicode 字符串。您能明確地發送該消息或用 [Editor\_DocGetConfigW](../macro/editor_docgetconfigw) 內嵌函式或
[Editor\_GetConfigW](../macro/editor_getconfigw)
內嵌函式。

EE\_GET\_CONFIGW

wParam = MAKEWPARAM(0, (iDoc)+1);

lParam = (LPARAM) (LPWSTR) szConfigName;

## 參數

_iDoc_

> 指定目標文檔的索引。應當指定一個從 1 開始的索引在 wParam 參數的高字處。如果 wParam 參數的高字處指定了 0，那么當前活動的文檔就會成為目標文檔。

_szConfigName_

> 指定會接收配置名稱的一個緩沖區。緩沖區大小必須至少是 MAX\_CONFIG\_NAME 的單詞數。

## 返回值

> 不使用返回值。