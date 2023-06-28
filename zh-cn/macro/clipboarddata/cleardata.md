# clearData 方法

从剪贴板上删除一个或多个数据格式。

#### \[JavaScript\]

clipboardData. **clearData**( \[ _sDataFormat_, \[ _iPos_ \] \] );

#### \[VBScript\]

clipboardData. **clearData** \[ _sDataFormat_, \[ _iPos_ \] \]

## 参数

_sDataFormat_

可选项。指定一个或多个下列数据格式值的字符串。如果省略，所有可用的格式都会被删除。

|     |     |
| --- | --- |
| Text | 删除所有格式包括文本。 |
| LineText | 删除行文本格式。 |
| BoxText | 删除框文本格式。 |

_iPos_

可选项。在剪贴板记录中指定位置如果你想要删除旧的剪贴板记录。如果这个参数是零或被省略，当前的数据会被删除。

## 示例

#### \[JavaScript\]

clipboardData.clearData();

#### \[VBScript\]

clipboardData.clearData

## 版本

支持 EmEditor 5.00 或之后的版本。