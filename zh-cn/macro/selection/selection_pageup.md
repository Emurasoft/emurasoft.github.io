# PageUp 方法 (Selection 对象)

在文档中，把光标上移指定的页数。

## 

### \[JavaScript\]

```
document.selection.PageUp( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.PageUp [ bExtend [, nCount ] ]
```

## 参数

_bExtend_

可选项。指定是否折叠被移动的文本。默认的值为 false，并且所移动的文本被折叠。

_nCount_

可选项。指定上移的页数。默认值是 1。如果指定的是负数，该方法与 [**PageDown** 方法](selection_pagedown) 相同。如果指定值为 0，该方法的行为与指定值为 1 时的行为相同。

## 版本

支持 EmEditor 4.00 或之后的版本。
