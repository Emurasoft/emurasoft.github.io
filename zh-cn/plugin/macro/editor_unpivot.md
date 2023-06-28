# Editor\_Unpivot

通过平展 CSV 数据将列转换为行。你能直接用该内联函数或明确地发送 [EE\_UNPIVOT](../message/ee_unpivot) 消息。

HRESULT Editor\_Unpivot( HWND hwnd, LPCWSTR pszSelect, LPCWSTR pszAttrLabel, LPCWSTR pszValueLabel, int nFooter );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pszSelect_

> 指定用于选择要逆透视的列的字符串。例如，"2-5", "3-", "1,3,5"。此字段不能为空。

_pszAttrLabel_

> 指定要创建的属性列的标题标签。

_pszValueLabel_

> 指定要创建的值列的标题标签。

_nFooter_

> 指定页脚中的行数。页脚行不会被转换。

## 返回值

> 如果失败，返回值为负值。

## 版本

> 支持 EmEditor Professional 21.4 或之后的版本。