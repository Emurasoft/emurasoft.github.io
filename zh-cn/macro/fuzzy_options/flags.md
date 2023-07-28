# Flags 属性 (FuzzyOptions 对象)

设置或检索标志。

该值必须为零或以下值的组合。

|     |     |
| --- | --- |
| eeFuzzyIgnoreCombining | 忽略组合字符，例如变音符号、dakuten（日文中的浊点）和 handakuten（日文中的半浊点）。 |
| eeFuzzyIgnoreEmoji | 忽略表情符号（emoji）序列。 |
| eeFuzzyIgnoreKanaSize | 忽略大假名和小假名之间的区别。 |
| eeFuzzyIgnoreKanaType | 忽略平假名与片假名字符之间的区别。 |
| eeFuzzyIgnoreVS | 忽略变体选择符。 |
| eeFuzzyIgnoreWidth | 忽略忽略半角和全角字符的区别。全角形式是中文和日文脚本中使用的独特格式。 |

## 

### \[JavaScript\]

```
n = obj.Flags;
obj.Flags = n;
```

### \[VBScript\]

```
n = obj.Flags;
obj.Flags = n;
```

## 版本

支持 EmEditor Professional Version 22.0 或之后的版本。
