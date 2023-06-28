# setData 方法

以指定格式分配数据到剪贴板上。

#### \[JavaScript\]

_bSuccess_ = clipboardData. **setData**( _sDataFormat_, _sData_, _iPos_ );

#### \[VBScript\]

_bSuccess_ = clipboardData. **setData**( _sDataFormat_, _sData, iPos_ )

## 参数

_sDataFormat_

指定一个或多个下列数据格式值得字符串。

|     |     |
| --- | --- |
| Text | 指定文本格式。 |
| LineText | 指定行文本格式。 |
| BoxText | 指定框文本格式。 |

_sData_

把文本数据指定为字符串。

_iPos_

可选。指定剪贴板记录中的位置如果你想要设置更旧的剪贴板数据。如果该值是零或被省略，会分配当前数据。

## 示例

#### \[JavaScript\]

clipboardData.setData("Text", "Hello!");

#### \[VBScript\]

clipboardData.setData "Text", "Hello!"

## 版本

支持 EmEditor 5.00 或之后的版本。