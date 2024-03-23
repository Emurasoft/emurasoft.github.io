# Flags Property (Filter Object)

Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeFindLogicalOr | Specifies a logical disjunction (logical OR) to the previous level in case of multiple levels of the filter. |
| eeFindNegative | Shows the Filter toolbar and excludes the lines that match the specified string. |
| eeFindReplaceCase | Matches cases. |
| eeFindReplaceEscSeq | Uses escape sequences. Cannot be combined with eeFindReplaceRegExp. |
| eeFindReplaceOnlyWord | Matches only whole words. |
| eeFindReplaceRegExp | Uses a regular expression for the searched string. Cannot be combined with eeFindReplaceEscSeq. |

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

## Version

Supported on EmEditor Professional Version 16.0 or later.
