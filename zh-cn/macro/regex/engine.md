# Engine 属性 (Regex 对象)

设置会检索正则表达式引擎类型。

该值必须是下列值之一。

|     |     |
| --- | --- |
| 0 | 使用默认正则表达式引擎。 |
| eeExFindRegexBoost | 把 Boost.Regex 作为正则表达式引擎。 |
| eeExFindRegexOnigmo | 把 Onigmo 作为正则表达式引擎。 |

## 

### \[JavaScript\]

```
n = reg.Engine;
reg.Engine = n;
```

### \[VBScript\]

```
n = reg.Engine;
reg.Engine = n;
```

## 版本

支持 EmEditor Professional Version 15.9 或之后的版本。
