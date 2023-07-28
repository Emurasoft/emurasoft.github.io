# DeleteLeft 方法 (Selection 对象)

删除所选内容。如果选定内容是空的，那么删除光标左边的指定字符数。

## 

### \[JavaScript\]

```
document.selection.DeleteLeft( [ nCount ] );
```

### \[VBScript\]

```
document.selection.DeleteLeft [ nCount ]
```

## 参数

_nCount_

可选项。指定光标左边要删除的字符数。默认值为 1。如果指定的是负数，那这个方法与 [**Delete** \
方法](selection_delete) 的行为相同。如果指定的是 0，会删除光标往左的 1 个字符数。

## 版本

支持 EmEditor 4.00 或之后的版本。
