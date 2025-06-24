# EE\_GET\_VERSION

返回版本號。您能明確地發送該消息或用 [Editor\_GetVersion](../macro/editor_getversion)
內嵌函式。

```
EE_GET_VERSION
wParam = pnProductType;
lParam = 0;
```

## 參數

_pnProductType_

指定一個指針指向整數值。這個消息返回下列值之一。

|     |     |
| --- | --- |
| VERSION\_PRO | EmEditor Professional |
| VERSION\_STD | EmEditor Standard |

## 返回值

返回被乘以 10000 的版本號。例如，如果版本號為 25.1.907，則返回值將為 251907。
