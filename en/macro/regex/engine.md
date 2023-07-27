# Engine Property (Regex Object)

Sets or retrieves the type of the regular expression engine.

The value must be one of the following values.

|     |     |
| --- | --- |
| 0 | Uses the default regular expression engine. |
| eeExFindRegexBoost | Uses Boost.Regex as the regular expression engine. |
| eeExFindRegexOnigmo | Uses Onigmo as the regular expression engine. |

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

## Version

Supported on EmEditor Professional Version 15.9 or later.
