# LineColumnMode 属性 (GeneralProp ����)

与配置属性中 [常规 页面](../../dlg/properties/general/index) 上的行列显示 下拉列表框相对应。

## 

### \[JavaScript\]

```
n Mode = object.LineColumnMode;
object.LineColumnMode = nMode;
```

### \[VBScript\]

```
nMode = object.LineColumnMode
object.LineColumnMode = nMode
```

## 参数

_nMode_

从下列值中选择。

|     |     |
| --- | --- |
| eeLineColumnView | 行号和列位置会以被显示的方式计数。如果换行，那么被换行的位置也会被计算在内。列的位置会在换行处被还原为 1。一个全角的字符计为 2 。这是如同文字处理器一样的显示方式。 |
| eeLineColumnLogicalA | 用真正的逻辑行号来计算行号和列位置。行号与列位置不取决于换行方式。一个全角字符被计为 2 列。一个制表符字符被计为 1 个字符。 |
| eeLineColumnLogicalW | 用真正的逻辑行行号来计算行号和列位置。行号与列位置不取决于换行方式。一个全角字符被计为 1 列。一个制表符字符被计为 1 个字符。 |
| eeLineColumnTabA | 用真正的逻辑行行号来计算行号和列位置。行号与列位置不取决于换行方式。一个全角字符被计为 2 列。当计数一个制表符字符时，就当它是用空格代替的。 |

## 版本

支持 EmEditor 7.00 或之后的版本。
