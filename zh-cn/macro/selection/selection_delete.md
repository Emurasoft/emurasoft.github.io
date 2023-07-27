# Delete 方法 (Selection ����)

删除所选内容。如果选定内容是空的，删除光标右边的指定字符数。

## 

### \[JavaScript\]

```
document.selection.Delete( [[ nCount ], bComplete ] );
```

### \[VBScript\]

```
document.selection.Delete [[ nCount ], bComplete ]
```

## 参数

_nCount_

可选项。指定光标右边要删除的字符数。默认值为 1。如果指定的是负数，那这个方法与 [DeleteLeft \
方法](selection_deleteleft) 的行为相同。如果指定的是 0，会删除光标往右的 1 个字符数。

_bComplete_

可选项。指定在单元格选择模式中是否要完全删除选区。如果省略，指定 True。

## 版本

支持 EmEditor 4.00 或之后的版本。
