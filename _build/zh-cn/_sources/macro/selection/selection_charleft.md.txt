# CharLeft 方法

把光标向左移动指定的字符数。

#### \[JavaScript\]

document.selection. **CharLeft**( \[ _bExtend_ \[, _nCount_ \] \] );

#### \[VBScript\]

document.selection. **CharLeft** \[ _bExtend_ \[, _nCount_ \] \]

## 参数

_bExtend_

可选项。指定是否折叠被移动的文本。默认的值为 false，并且所移动的文本被折叠。

_nCount_

可选项。指定向左移动的字符数。默认值是 1。如果指定的是负数，该方法与 [**CharRight** \
方法](selection_charright) 的行为相同。如果指定的是 0，会向左移动 1 个字符。

## 版本

支持 EmEditor 4.00 或之后的版本。