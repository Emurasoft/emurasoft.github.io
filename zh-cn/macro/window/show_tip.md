# ShowTip 方法 (Window 对象)

显示工具提示。

## 

### \[JavaScript\]

```
ShowTip( strTip, flags );
```

### \[VBScript\]

```
ShowTip strTip, flags
```

## 参数

_strTip_

指定要在工具提示中显示的文本。文本长度不能超过 3,999 个字符。该字符串可包含以这种格式指定的可点击文本："<a href="url">可点击文本</a>"。

_flags_

指定下列值之一。

|     |     |
| --- | --- |
| eeShowTipActiveString | 在鼠标悬停的活动字符串处显示工具提示。 |
| eeShowTipCurrentCaret | 在插入符号位置显示工具提示。 |
| eeShowTipCurrentMouse | 在鼠标指针位置显示工具提示。 |
| eeShowTipHide | 如果已经显示，隐藏工具提示。 |

## 版本

支持 EmEditor 16.9 或之后的版本。
