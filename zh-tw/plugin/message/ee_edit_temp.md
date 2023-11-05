# EE\_EDIT\_TEMP

把臨時文本作為一個新文檔打開，或激活、保存或關閉已存在的臨時文本。您能明確地發送該消息或用 [Editor\_ActivateTemp](../macro/editor_activatetemp)， [Editor\_CloseTemp](../macro/editor_closetemp)，
[Editor\_EditTemp](../macro/editor_edittemp)，或 [Editor\_SaveTemp](../macro/editor_savetemp) 內嵌函式。

```
EE_EDIT_TEMP
wParam = 0;
lParam = (LPARAM) (TEMP_INFO) pTI;
```

## 參數

_pTI_

指針指向 [TEMP\_INFO](../structure/temp_info) 結構。

## 返回值

返回值是新文檔的 ID。然而，當關閉一個臨時文本時，不使用返回值。

## 支持版本

支持 EmEditor 9.00 或之後的版本。
