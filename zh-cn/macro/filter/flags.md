# Flags 属性 (Filter 对象)

指定下列值的组合。

|     |     |
| --- | --- |
| eeFindLogicalOr | 指定一个逻辑或运算 (logical OR) 到之前的层级上在多层级筛选的情况下。 |
| eeFindNegative | 显示筛选工具栏并排除与指定字符串匹配的行。 |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceEscSeq | 使用转义符。不能与 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整个单词需匹配。 |
| eeFindReplaceRegExp | 使用正则表达式搜索字符串。不能与 eeFindReplaceEscSeq 合用。 |

## 

### \[JavaScript\]

```
flag = item.Flags;
item.Flags = flags;
```

### \[VBScript\]

```
n = item.Flags
item.Flags = n
```

## 版本

支持 EmEditor Professional Version 16.0 或之后的版本。
