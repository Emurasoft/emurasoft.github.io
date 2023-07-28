# WordLeft 方法 (Selection 对象)

把光标向左移指定的单词数。

## 

### \[JavaScript\]

```
document.selection.WordLeft( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.WordLeft [ bExtend [, nCount ] ]
```

## 参数

_bExtend_

可选项。指定是否折叠被移动的文本。默认的值为 false，并且所移动的文本被折叠。

_nCount_

可选项。指定向左移的单词数。默认值是 1。如果指定的是负数，该方法与 [WordRight \
方法](selection_wordright) 的行为相同。如果指定值为 0，该方法的行为与指定值为 1 时的行为相同。

## 版本

支持 EmEditor 4.00 或之后的版本。
