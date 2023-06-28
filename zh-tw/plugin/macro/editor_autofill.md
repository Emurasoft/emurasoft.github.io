# Editor\_AutoFill

對 CSV 文檔執行自動填滿或快速填入操作。你能直接用該內嵌函式或明確地發送 [EE\_AUTOFILL](../message/ee_add_ref) 消息。

Editor\_AutoFill( HWND hwnd, AUTOFILL\_INFO\* pInfo );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控點。

_hInstance_

> 指針指向 [AUTOFILL\_INFO](../structure/autofill_info) 結構。

## 返回值

> 如果消息成功，則返回值可以是以下值的組合。返回值 0 意味著消息無法檢測到模式以完成自動填滿或快速填入操作。負值表示消息失敗。
>
> |     |     |
> | --- | --- |
> | S\_FILL\_COPY | 將源範圍中的值複製到目標範圍，必要時重複。 |
> | S\_FILL\_SERIES | 將源範圍中的值作為一數列延伸到目標範圍。 |
> | S\_FILL\_FLASH | 執行快速填入操作，即根據檢測到的模式將源範圍中的值延伸到目標範圍。該標志僅適用於垂直方向。 |

## 版本

> 支持 EmEditor 17.5 或之後的版本。