# EE\_RUN\_MACRO

運行一個巨集。您能明確地發送該消息或用 [Editor\_RunMacro](../macro/editor_runmacro)
內嵌函式。

EE\_RUN\_MACRO

wParam = 0;

lParam = (LPARAM) (RUN\_MACRO\_INFO\*) pRMI;

## 參數

_pRMI_

Pointer to the [RUN\_MACRO\_INFO](../structure/run_macro_info) 結構。

## 返回值

返回值是下列值之一。

|     |     |
| --- | --- |
| S\_OK | 成功。 |
| S\_FALSE | 存在一個巨集錯誤，如語法錯誤。 |
| S\_EDIT\_TEMP | 存在一個巨集錯誤，但無法打開源代碼來編輯因為源代碼不是一個文本檔案。調用方應當用被按照 ptErrorPos 參數提供的信息設置的光標位置來打開源檔案。 |
| E\_FAIL | 存在一個嚴重錯誤。 |

## 支持版本

支持 EmEditor 9.00 或之後的版本。
