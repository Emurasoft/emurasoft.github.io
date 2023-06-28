# WrapMode 属性

与配置属性中 [**常规** 页面](../../dlg/properties/general/index) 上的 **自动换行** 下拉列表框相对应。

#### \[JavaScript\]

_nMode_ =
object. **WrapMode**;

object. **WrapMode** = _nMode_;

#### \[VBScript\]

_nMode_ =
object. **WrapMode**

object. **WrapMode** = _nMode_

## 参数

_nMode_

从下列值中选择。

|     |     |
| --- | --- |
| eeWrapNone | 不换行。 |
| eeWrapByChar | 按指定字符长度（字节数）换行。字符长度能在 [**标准行边距** 文本框](../../dlg/properties/general/index) 或 [**引用行边距** 文本框](../../dlg/properties/general/index) 中指定。 |
| eeWrapByWindow | 按窗口宽度换行。如果窗口的大小被重新调整，换行的位置也会被调整。 |
| eeWrapByPage | 按打印的页面宽度换行。 |

## 版本

支持 EmEditor 7.00 或之后的版本。