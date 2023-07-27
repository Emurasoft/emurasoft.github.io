# Flags 屬性 (Filter ��H)

指定下列值的組合。

|     |     |
| --- | --- |
| eeFindLogicalOr | 指定一個邏輯分離 (logical OR) 到之前的層級上在多層級篩選的情況下。 |
| eeFindNegative | 顯示篩選工具列并排除與指定字串符合的行。 |
| eeFindReplaceCase | 大小寫需符合。 |
| eeFindReplaceEscSeq | 使用逸出序列。不能與 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整個單字需符合。 |
| eeFindReplaceRegExp | 使用規則運算式搜索字串。不能與 eeFindReplaceEscSeq 合用。 |

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

支持 EmEditor Professional Version 16.0 或之後的版本。
