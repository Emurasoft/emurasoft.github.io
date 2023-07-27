# Editor\_AutoFill

对 CSV 文档执行自动填充或快速填充操作。你能直接用该内联函数或明确地发送 [EE\_AUTOFILL](../message/ee_add_ref) 消息。

Editor\_AutoFill( HWND hwnd, AUTOFILL\_INFO\* pInfo );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_hInstance_

指针指向 [AUTOFILL\_INFO](../structure/autofill_info) 结构。

## 返回值

如果消息成功，则返回值可以是以下值的组合。返回值 0 意味着消息无法检测到模式以完成自动填充或快速填充操作。负值表示消息失败。

|     |     |
| --- | --- |
| S\_FILL\_COPY | 将源范围中的值复制到目标范围，必要时重复。 |
| S\_FILL\_SERIES | 将源范围中的值作为一序列扩展到目标范围。 |
| S\_FILL\_FLASH | 执行快速填充操作，即根据检测到的模式将源范围中的值扩展到目标范围。该标志仅适用于垂直方向。 |

## 版本

支持 EmEditor 17.5 或之后的版本。
