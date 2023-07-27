# InsertDate 方法 (Selection ����)

插入当前时间和日期。

## 

### \[JavaScript\]

```
document.selection.InsertDate( nFlags );
```

### \[VBScript\]

```
document.selection.InsertDate [ nFlags ]
```

## 参数

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeDateTimeDate | 指定时间，后跟一个空格，然后日期。 |
| eeDateDateTime | 指定日期，后跟一个空格，然后时间。 |

## 备注

用于时间与日期的格式能在 Windows 上被配置，通过到控制面板 中的区域语言选项 上，然后选择日期与时间。

## 版本

支持 EmEditor 4.00 或之后的版本。
