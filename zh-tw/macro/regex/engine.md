# Engine 屬性 (Regex 對象)

設置會檢索規則運算式引擎類型。

該值必須是下列值之一。

|     |     |
| --- | --- |
| 0 | 使用預設規則運算式引擎。 |
| eeExFindRegexBoost | 把 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 把 Onigmo 作為規則運算式引擎，Ruby 語法。 |
| eeExFindRegexOnigmoPerl | 使用 Onigmo 作為規則運算式引擎，Perl 語法。 |

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

支持 EmEditor Professional Version 15.9 或之後的版本。
