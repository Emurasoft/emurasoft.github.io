# EE\_RUN\_MACRO

运行一个宏。你能明确地发送该消息或用 [Editor\_RunMacro](../macro/editor_runmacro)
内联函数。

EE\_RUN\_MACRO

wParam = 0;

lParam = (LPARAM) (RUN\_MACRO\_INFO\*) pRMI;

## 参数

_pRMI_

Pointer to the [RUN\_MACRO\_INFO](../structure/run_macro_info) 结构。

## 返回值

返回值是下列值之一。

|     |     |
| --- | --- |
| S\_OK | 成功。 |
| S\_FALSE | 存在一个宏错误，如语法错误。 |
| S\_EDIT\_TEMP | 存在一个宏错误，但无法打开源代码来编辑因为源代码不是一个文本文件。调用方应当用被按照 ptErrorPos 参数提供的信息设置的光标位置来打开源文件。 |
| E\_FAIL | 存在一个严重错误。 |

## 支持版本

支持 EmEditor 9.00 或之后的版本。
