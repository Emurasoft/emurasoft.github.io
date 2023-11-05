# EE\_EXTRACT\_FREQUENT

将常用字符串提取到新文档中。你可以明确地发送该消息或用 [Editor\_ExtractFrequent](../macro/editor_extractfrequent) 内联函数。

```
EE_EXTRACT_FREQUENT
wParam = (WPARAM) (EXTRACT_FREQUENT_INFO*) pInfo;
lParam = 0;
```

## 参数s

_pInfo_

指针指向 [EXTRACT\_FREQUENT\_INFO 结构](../structure/extract_frequent_info)。

## 返回值

如果发生错误，则返回值为负。

## 版本

支持 EmEditor Professional Version 21.9 或之后的版本。
