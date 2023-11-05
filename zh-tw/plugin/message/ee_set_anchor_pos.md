# EE\_SET\_ANCHOR\_POS

設置選區的原點。您能明確地發送該消息或用 [Editor\_SetAnchorPos](../macro/editor_setanchorpos)
內嵌函式。

```
EE_SET_ANCHOR_POS
wParam = (WPARAM) (int) nLogical;
lParam = (LPARAM) (POINT_PTR*) pptPos;
```

## 參數

_nLogical_

指定下列值之一。

| 值 | 含義 |
| --- | --- |
| POS\_VIEW | 顯示坐標 |
| POS\_LOGICAL\_A | 邏輯坐標 (把雙位元字元計為兩個) |
| POS\_LOGICAL\_W | 邏輯坐標 (把雙位元字元計為一個) |
| POS\_CELL | CSV 儲存格單位 |

_pptPos_

指針指向一個指定選區原點的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

不使用返回值。
