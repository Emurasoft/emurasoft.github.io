# EE\_OUTPUT\_DIR

为输出栏设置当前目录。你能明确地发送该消息或用 [Editor\_OutputDir](../macro/editor_outputdir) 内联函数。

```
EE_OUTPUT_DIR
wParam = 0;
lParam = (LPARAM) (LPCWSTR) szCurrDir;
```

## 参数

_szCurrDir_

指定当前目录。该信息是必需的如果文本含有一个只能从当前目录上跳转的、可点击的相对路径。

## 返回值

不使用返回值。

## 支持版本

支持 EmEditor 7.00 或之后的版本。
