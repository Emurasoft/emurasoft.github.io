# StartOfLine 方法 (Selection 对象)

把光标移动到行首。

## 

### \[JavaScript\]

```
document.selection.StartOfLine( [ bExtend [, nFlags ] ]
);
```

### \[VBScript\]

```
document.selection.StartOfLine [ bExtend [, nFlags ] ]
```

## 参数

_bExtend_

可选项。指定是否折叠被移动的文本。默认的值为 false，并且所移动的文本被折叠。

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeLineView | 指定显示行。 |
| eeLineLogical | 指定逻辑行。 |
| eeLineHomeText | 移动到文本的开始位置，不算空格。 |

## 版本

支持 EmEditor 4.00 或之后的版本。
