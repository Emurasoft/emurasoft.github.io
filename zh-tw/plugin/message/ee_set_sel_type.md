# EE\_SET\_SEL\_TYPE

設置選區狀態的類型。您能明確地發送該消息或用 [Editor\_SetSelType](../macro/editor_setseltype) 內嵌函式或 [Editor\_SetSelTypeEx](../macro/editor_setseltypeex) 內嵌函式。

```
EE_SET_SEL_TYPE
wParam = (WPARAM) (BOOL) bNeedAlways;
lParam = (LPARAM) nSelType;
```

## 參數

_bNeedAlways_

如果該參數是 TRUE，您能設置選區狀態的類型即使沒有選取任何文本。如果該參數是 FALSE，SEL\_TYPE\_NONE 將會取消對選擇部分的選取。

_nSelType_

您能從如下值中指定一個組合。然而，SEL\_TYPE\_NONE，SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，SEL\_TYPE\_BOX 不能聯合使用。只有 SEL\_TYPE\_KEYBOARD 可以與 SEL\_TYPE\_NONE，
SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，或 SEL\_TYPE\_BOX一起使用。

|     |     |
| --- | --- |
| SEL\_TYPE\_NONE | 沒有選擇。 |
| SEL\_TYPE\_CHAR | 流選擇模式。 |
| SEL\_TYPE\_LINE | 行選擇模式。 |
| SEL\_TYPE\_BOX | 垂直選擇模式。 |
| SEL\_TYPE\_KEYBOARD | 指定鍵盤選擇模式。這個值能與另一個值進行組合。 |

## 返回值

不使用。

## 支持版本

支持 EmEditor 3.00 或之後的版本。然而，bNeedAlways 支持 EmEditor 5.00 或之後的版本。在前幾個版本中，bNeedAlways 被假定為 FALSE。
