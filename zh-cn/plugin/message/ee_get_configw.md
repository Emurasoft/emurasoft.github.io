# EE\_GET\_CONFIGW

检索所选取的配置名称为 Unicode 字符串。你能明确地发送该消息或用 [Editor\_DocGetConfigW](../macro/editor_docgetconfigw) 内联函数或
[Editor\_GetConfigW](../macro/editor_getconfigw)
内联函数。

```
EE_GET_CONFIGW
wParam = MAKEWPARAM(0, (iDoc)+1);
lParam = (LPARAM) (LPWSTR) szConfigName;
```

## 参数

_iDoc_

指定目标文档的索引。应当指定一个以 1 为基准的索引在 wParam 参数的高字处。如果 wParam 参数的高字处指定了 0，那么当前活动的文档就会成为目标文档。

_szConfigName_

指定会接收配置名称的一个缓冲区。缓冲区大小必须至少是 MAX\_CONFIG\_NAME 的单词数。

## 返回值

不使用返回值。
