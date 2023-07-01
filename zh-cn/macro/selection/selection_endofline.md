# EndOfLine 方法 (Selection ����)

把光标移到当前行的尾端。

#### \[JavaScript\]

document.selection. **EndOfLine**( \[ _bExtend_ \[, _nFlags_ \] \] );

#### \[VBScript\]

document.selection. **EndOfLine** \[ _bExtend_ \[, _nFlags_ \] \]

## 参数

_bExtend_

可选项。指定是否折叠被移动的文本。默认的值为 false，并且所移动的文本被折叠。

_nFlags_

可选项。指定一个下列值得组合:

|     |     |
| --- | --- |
| eeLineView | 指定显示行。 |
| eeLineLogical | 指定逻辑行。 |

## 版本

支持 EmEditor 4.00 或之后的版本。
